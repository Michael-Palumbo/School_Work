#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

#define PATH_LENGTH 64
#define INPUT_LENGTH 128

void parseCommand(char *);
//char** tokenize(char *);
void simpleTokenize(char *, char **); 

int last_pid = 0;
void resetPid();

int
main(int argc, char *argv[]){
	char cwd[PATH_LENGTH];
	char input[INPUT_LENGTH];


	printf("==================\n");
	printf("Opened up C Shell\n");
	printf("==================\n");

	for(;;){
		if(getcwd(cwd, sizeof(cwd)) != NULL){
			
			printf("%s: ",cwd);
			fgets(input, INPUT_LENGTH, stdin);
			input[ strlen(input) - 1 ] = '\0';	

			if(feof(stdin)){
				printf("Thank you\n");
				return 0;
			}

			parseCommand(input);
		}else{
			perror("getcwd error");
			exit(1);
		}
	}
}

void
parseCommand(char *inp){
	int status;
	int notWaiting = 0;
	char copy[INPUT_LENGTH];
	char *tokens[32];

	if(inp[strlen(inp) - 1] == '&'){
		inp[strlen(inp) - 1] = '\0';
	      	notWaiting = 1;	
	}

	strcpy(copy, inp);	
	
	//It seems strtok is changing inp, so i decided to send it a copy instead
	simpleTokenize(copy, tokens);

	/*
	printf("List of tokens:\n");
	
	for(int i = 0; tokens[i] != NULL; i++) 
		printf("%d: %s\n",i, tokens[i]);
	*/

	if(!strcmp(tokens[0], "cd")){
		chdir(inp+3);
		return;
	}

	if(last_pid != 0)
		resetPid();

	int pid = fork();
	
	if(pid < 0){
		perror("Fork");
		exit(4);
	}else if(pid == 0){
		execvp(tokens[0], tokens);
		perror("exec");
		exit(3);
	}else if(pid > 0 && notWaiting == 0){ //if notWaiting is false
		wait(&status);
	}else{
		last_pid = pid;
	}

	return;
}

void 
resetPid(){
	int status2;
	wait(&status2);
	last_pid = 0;
}

void
simpleTokenize(char *inp, char ** tokens){
	tokens[0] = strtok(inp, " ");

	for(int i = 1; i < 32; i++){
		tokens[i] = strtok(NULL, " ");
		if(tokens[i] == NULL) break;
	}	
}
