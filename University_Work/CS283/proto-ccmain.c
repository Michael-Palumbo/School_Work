#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

void runFunction(char *);

int
main(int argc, char *argv[]){
	
	printf("Weclome to our item ordering jawn\n");
	printf("1.ccadd\n");
	printf("2.ccitem\n");
	printf("3.cclist\n");
	printf("4.ccdel\n");
	printf("5.ccmatch\n");
	printf("6.ccyear\n");
	printf("7.ccedit\n");
	printf("8.Quit\n");
	printf("What action would you like to take? :");

	switch(getchar() - '0'){
		case 0:
			printf("test reached\n");
			runFunction("test abc");
			break;
		case 1:
			runFunction("ccadd.o");
			break;
		case 2:
			runFunction("ccitem.o");
			break;
		case 3:
			runFunction("cclist.o");
			break;
		case 4:
			runFunction("ccdel.o");
			break;
		case 5:
			runFunction("ccmatch.o");
			break;
		case 6:
			runFunction("ccyear.o");
			break;
		case 7:
			runFunction("ccedit.o");
			break;
		case 8:
			printf("Thank you, Cya later\n");
			exit(0);
		default:
			printf("Cannot find input, please use a listed number");
			break;

	}

	exit(0);
}

void
runFunction(char *s){
	int status;
	if(fork() > 0){
		wait(&status);
		printf("after the wait reached\n value of string: $%s$\n",s);
	}
	else{
		printf("runFunction reached: $%s$\n",s);
		char string[10];
		strcpy(string,s);
		char *tokens[32];
		tokens[0] = strtok(string, " ");
		printf("tokens[0]: $%s$",tokens[0]);
		for (int i = 1; i < 10; i++){
			tokens[i] = strtok(NULL, " ");
			if(tokens[i] == NULL){ printf("first for:%s %d\n",tokens[i],i); break;}
		}
		
		for(int i = 0; tokens[i] != NULL; i++)
			fprintf(stderr, "%s\n", tokens[i]);
		
		execv(tokens[0], tokens);
		perror("exec");
		exit(4);
	}
}
