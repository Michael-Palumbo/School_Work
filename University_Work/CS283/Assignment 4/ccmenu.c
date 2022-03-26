#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

void runFunction(char *, char **);

int
main(int argc, char *argv[]){
	char c;
	char *pargs[10];
	for(int i = 0; i < 10; i++)
		pargs[i] = malloc(128 * sizeof(char));

	while(1){
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
		//scanf("%c", &c);
		c = getchar();
		switch(c - '0'){
			case 1:
				printf("pass argument for id: ");
				scanf("%s",pargs[1]);
				printf("pass argument for maker: ");
				scanf("%s",pargs[2]);
				printf("pass argument for model: ");
				scanf("%s",pargs[3]);
				printf("pass argument for year: ");
				scanf("%s",pargs[4]);
				printf("pass argument for cpu: ");
				scanf("%s",pargs[5]);
				printf("pass argument for desc: ");
				scanf("%s",pargs[6]);
				
				pargs[7] = NULL;
				runFunction("ccadd.o", pargs);
				break;
			case 2:
				printf("pass argument for id: ");
				scanf("%s", pargs[1]);

				pargs[2] = NULL;
				runFunction("ccitem.o", pargs);
				break;
			case 3:
				pargs[1] = NULL;
				runFunction("cclist.o", pargs);
				break;
			case 4:
				printf("pass argument for id: ");
				scanf("%s", pargs[1]);

				pargs[2] = NULL;
				runFunction("ccdel.o", pargs);
				break;
			case 5:
				printf("pass argument for string: ");
				scanf("%s", pargs[1]);
				
				pargs[2] = NULL;
				runFunction("ccmatch.o", pargs);
				break;
			case 6:
				printf("pass argument for start year: ");
				scanf("%s", pargs[1]);
				printf("pass argument for end year: ");
				scanf("%s", pargs[2]);
	
				pargs[3] = NULL;
				runFunction("ccyear.o", pargs);
				break;
			case 7:
				printf("pass argument for id: ");
				scanf("%s", pargs[1]);
				
				pargs[2] = NULL;
				runFunction("ccedit.o", pargs);
				break;
			case 8:
				printf("Thank you, Cya later\n");
				exit(0);
			default:
				printf("Cannot find input, please use a listed number\n");
				break;
		}
	}
	exit(0);
}

void
runFunction(char *prog, char **arg){
	int status;

	arg[0] = prog;
	
	//printf("%d arg is : %s$\n",0, arg[0]);
	//printf("%d arg is : %s$\n",1, arg[1]);
	
	if(fork() > 0){
		wait(&status);
	}
	else{	
		execv(arg[0], arg);
		perror("exec");
		exit(4);
	}
	
}
