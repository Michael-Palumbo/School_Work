#include <stdio.h>
#include <string.h>

void trim(char *);

int
main(int argc, char *argv[]){
	char *readOnly = "";
	char writeTo[64];

	strcpy(writeTo,readOnly);

	printf("Original: $%s$\n", writeTo);

	trim(writeTo);

	printf("New: $%s$\n", writeTo);
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