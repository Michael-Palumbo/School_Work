#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	if(argc == 1){
		printf("No argument given!\n");
		return 1;
	}
	FILE *file = fopen(argv[1], "r");
	if(file == NULL){
		printf("Cannot find image\n");
		return 2;
	}
	char* n = malloc(strlen("test") + strlen(argv[1]) + 1);
	strcpy(n,"test");
	strcat(n,argv[1]);
	printf("%s\n",n);
	fclose(file);

	return 0;

}
