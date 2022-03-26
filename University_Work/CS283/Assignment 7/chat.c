#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <string.h>

void *sender(void *);
void *writer(void *);

pthread_mutex_t client_lock;

int
main(int argc, char *argv[]){

	if(argc != 2){
		perror("Usage Error: chat name");
		exit(2);
	}

	int sock;
	struct sockaddr_in listener;

	pthread_t tid;
	pthread_mutex_init(&client_lock, NULL);

	/* AF_INET: Adress Family of Inet (internet), the protocol suite we are looking at.
	 * SOCK_STREAM: type of connection, dcp connection */
	sock = socket(AF_INET, SOCK_STREAM, 0);

	listener.sin_family = AF_INET;
	//Host to Network of type short. Needs to be more than 1024 (since below is special)
	listener.sin_port = htons(2020); 
	//sin_addr is another struct of type s_addr. 
	//The address information we bind to the socket
	listener.sin_addr.s_addr = htonl(INADDR_LOOPBACK);//htonl(INADDR_ANY); 

	/* Binding, We need a socket, a sockaddr that we will listen with, and a length 
	 * After this command, we can now use sock to listen to incoming connections */
	// if( bind(sock, (struct sockaddr *)&listener, sizeof(struct sockaddr_in)) < 0 ){
	// 	perror("bind");
	// 	exit(1);
	// }

	// Need to call connect 
	if( connect( sock, (struct sockaddr *)&listener, sizeof(struct sockaddr_in)) < 0){
		perror("connect");
		exit(2);
	}

	if(send(sock, argv[1], strlen(argv[1]) + 1, 0) <= 0){
		perror("username");
		exit(3);
	}
	
	pthread_create(&tid,NULL,sender, &sock);
	pthread_create(&tid,NULL,writer, &sock);

	pthread_join(tid, NULL);

}

void *
sender(void* arg){
	int* sock = arg;
	char buf[1024];
	int len;
	while(1){
		fgets(buf,1024,stdin);
		len = strlen(buf);
		if(send(*sock, buf, len+1, 0) <= 0){
			exit(2);
		}
	}
}

void *
writer(void* arg){
	int n;
	int* sock = arg;
	char buf[1024];
	while(1){
		if((n = recv(*sock, buf, 1024, 0)) <= 0){
			exit(3);
		}
		buf[n] = '\0';
		printf("%s",buf);
	}
}
