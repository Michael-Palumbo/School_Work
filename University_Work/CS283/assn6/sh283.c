#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>

#define PATH_LENGTH 64
#define INPUT_LENGTH 128


//Redirection Commands
int checkRedirections(char *, char *, char *);
void redirectIn(char *);
void redirectOut(char *, int);
void trim(char *);

//void seperateCommand(char *);
void parseCommand(char *);
void pipeCommand(char *);
//char** tokenize(char *);
void simpleTokenize(char *, char **, char*); 

int last_pid = 0;
void resetPid();

int
main(int argc, char *argv[]){
	char cwd[PATH_LENGTH];
	char input[INPUT_LENGTH];
	char *commands[32];

	printf("======================\n");
	printf(" Opened up C Shell v2\n");
	printf("======================\n");

	for(;;){
		if(getcwd(cwd, sizeof(cwd)) != NULL){
			
			//Print Prompt
			printf("%s: ",cwd);

			//Get User rinput
			fgets(input, INPUT_LENGTH, stdin);
			input[ strlen(input) - 1 ] = '\0';	//Probably useless

			//Check if user did ctrl+d
			if(feof(stdin)){
				printf("Thank you\n");
				return 0;
			}

			//Time to execute the code
			if(strchr(input, '&') != NULL){
				simpleTokenize(input, commands, "&");
				*(strchr(commands[0],'\0')-1) = '&';
				printf("command: %s\n", commands[0]);
					
			}else
				simpleTokenize(input, commands, ";");

			for(int i = 0; commands[i] != NULL; i++) 
				// if(commands[i] != NULL)
				if(strchr(input, '|'))
					pipeCommand(commands[i]);
				else
					parseCommand(commands[i]);

			//End of Executing the code
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

	int append = 0;
	char redIn[PATH_LENGTH];
	char redOut[PATH_LENGTH];

	//returns 1 if writing will be appended
	append = checkRedirections(inp,redIn,redOut);

	if(inp[strlen(inp) - 1] == '&'){
		inp[strlen(inp) - 1] = '\0';
	      	notWaiting = 1;	
	}

	strcpy(copy, inp);	
	
	simpleTokenize(inp, tokens, " \t\n");

	//Special excpetion for cd command
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

		if(strlen(redIn) != 0)
			redirectIn(redIn);
		if(strlen(redOut) != 0)
			redirectOut(redOut,append);

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
pipeCommand(char *inp){
	char copy[INPUT_LENGTH];
	int status;
	char *sides[2];
	char *tokens1[32];
	char *tokens2[32];
	int pfd[2];

	strcpy(copy, inp);

	simpleTokenize(inp, sides, "|");

	simpleTokenize(sides[0], tokens1, " \t\n");

	simpleTokenize(sides[1], tokens2, " \t\n");

	pipe(pfd);

	int pid = fork();

	if(pid < 0){
		perror("Fork");
		exit(4);
	}else if(pid == 0) {
		int pid2 = fork();
		if(pid2 < 0){
			perror("Fork");
			exit(4);
		}else if(pid2 == 0) {
			close(pfd[0]);
			close(1);
			dup(pfd[1]);
			execvp(tokens1[0], tokens1);
			perror("exec");
			exit(3);
		}else{
			close(pfd[1]);
			close(0);
			dup(pfd[0]);
			execvp(tokens2[0], tokens2);
			perror("exec");
			exit(3);
		}
	}else
		wait(&status);
}

int
checkRedirections(char *input, char *redIn, char *redOut){
	
	if(strchr(input,'<') != NULL){
		strcpy(redIn, strchr(input,'<')+1);
		input[strchr(input,'<')-input] = '\0';
	}else
		redIn[0] = '\0';

	if(strchr(input,'>') != NULL){
		if(*(strchr(input,'>')+1) == '>'){
			strcpy(redOut, strchr(input,'>')+2);
			input[strchr(input,'>')-input] = '\0';
			return 1;
		}
		strcpy(redOut, strchr(input,'>')+1);
		input[strchr(input,'>')-input] = '\0';
		return 0;
	}else if(strchr(redIn,'>') != NULL){
		if(*(strchr(input,'>')+1) == '>'){
			strcpy(redOut, strchr(input,'>')+2);
			input[strchr(input,'>')-input] = '\0';
			return 1;
		}
		strcpy(redOut, strchr(redIn,'>')+1);
		redIn[strchr(redIn,'>')-redIn] = '\0';
		return 0;
	}else{
		redOut[0] = '\0';
		return 0;
	}
}

void
redirectIn(char *redIn){
	trim(redIn);
	// int fd = open(redIn, O_RDONLY);
	int fd = fileno(fopen(redIn, "r"));
	close(0);
	dup(fd);
}

void
redirectOut(char *redOut, int append){
	trim(redOut);
	int fd;
	// int fd = open(redOut, O_WRONLY);
	if(append == 1)
		fd = fileno(fopen(redOut,"a"));
	else
		fd = fileno(fopen(redOut,"w+"));
	close(1);
	dup(fd);
}

void
simpleTokenize(char *inp, char ** tokens, char * delimiter){
	tokens[0] = strtok(inp, delimiter);

	for(int i = 1; i < 32; i++){
		tokens[i] = strtok(NULL, delimiter);
		if(tokens[i] == NULL) break;
	}	
}

void 
resetPid(){
	int status2;
	wait(&status2);
	last_pid = 0;
}

void
trim(char * str){
	char *start;
	char *end;

	//Look at start
	for(start = str; *start == ' '; start++);

	//Look at end
	for(end = strlen(str)+str-1; *end == ' '; end--);

	*(end + 1) = '\0';

	strcpy(str, start);
}