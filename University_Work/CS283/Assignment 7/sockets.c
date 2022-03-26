#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <string.h>

typedef struct Client Client;

struct Client{
	int sock;
	pthread_t tid;
	char name[16];
	Client *next, *prev;
};

void *client(void *);

Client *chead; //head of the linked list of clients
pthread_mutex_t client_lock;

int
main(int argc, char *argv){

	int sock;
	pthread_t tid;
	struct sockaddr_in listener;
	Client *c;

	pthread_mutex_init(&client_lock, NULL);

	/* AF_INET: Adress Family of Inet (internet), the protocol suite we are looking at.
	 * SOCK_STREAM: type of connection, dcp connection */
	sock = socket(AF_INET, SOCK_STREAM, 0);

	listener.sin_family = AF_INET;
	//Host to Network of type short. Needs to be more than 1024 (since below is special)
	listener.sin_port = htons(2020); 
	//sin_addr is another struct of type s_addr. 
	//The address information we bind to the socket
	listener.sin_addr.s_addr = htonl(INADDR_ANY); 

	/* Binding, We need a socket, a sockaddr that we will listen with, and a length 
	 * After this command, we can now use sock to listen to incoming connections */
	if( bind(sock, (struct sockaddr *)&listener, sizeof(struct sockaddr_in)) < 0 ){
		perror("bind");
		exit(1);
	}

	while(1){

		//listens on to a connection. later we have to accept or reject a connection
		if( listen(sock, 5) < 0){
			perror("listen");
			exit(2);
		}

		c = malloc(sizeof(Client));

		// We listen (above), once we are succesful we have to accept it
		// It returns the sock that we use to communicate to them
		c->sock = accept(sock, NULL, NULL);
		printf("Connected\n");

		if(c->sock < 0){
			perror("accept");
			free(c);
		}else{
			pthread_create(&tid, NULL, client, c);
		}
	}
}

void
cadd(Client *c){
	//when we have multiple threads, we need to lock before edditing data structures
	pthread_mutex_lock(&client_lock); 
	c->prev = NULL;
	if(chead != NULL){
		chead->prev = c;
	}
	c->next = chead;
	chead = c;
	pthread_mutex_unlock(&client_lock);
}

void
cdel(Client *c){
	if(chead == c){
		chead = c->next;
	}
	if(c->next != NULL){
		c->next->prev = c->prev;
	}
	if(c->prev != NULL){
		c->prev->next = c->next;
	}
}

void *
client(void *p){
	Client *c = p;
	Client *q, *r;

	char buf[1024];
	int n, prefix;

	c->tid = pthread_self();
	pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, &n);
	// Recieved a message
	n = recv(c->sock, buf, 1024, 0);
	if(n <= 0){
		free(c);
		pthread_exit(NULL);
	}
	if(n > 15)
		n = 15;
	strncpy(c->name, buf, n);
	c->name[n] = '\0';

	//number of bytes it writes, what index of buf to write the message to
	prefix = sprintf(buf,"%s> ",c->name);
	cadd(c);

	//recieves
	while(1){
		n = recv(c->sock, buf + prefix, 1024 - prefix, 0);
		if(n <= 0){
			pthread_mutex_lock(&client_lock);
			cdel(c);
			pthread_mutex_unlock(&client_lock);
			free(c);
			pthread_exit(NULL);
		}
		pthread_mutex_lock(&client_lock);
		for(q=chead; q!=NULL; q = q->next){
			if(q != c){
				if(send(q->sock, buf, n + prefix, 0) <= 0){
					pthread_cancel(q->tid);
					cdel(q);
					r = q;
					q = q->next;
					free(r);
				}
			}
		}
		pthread_mutex_unlock(&client_lock);
	}
}
