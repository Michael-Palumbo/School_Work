#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include "cc.h"


int 
requestValue(char *str){

	printf("Would you like the change the value of %s? y/n\n", str);
	return getchar() == 'y';
	

}

void
getResponse(char *response){	
	printf("What value would you like to change it to?\n");
	scanf("%s",response);
}
int 
main(int argc, char *argv[]){
	
	CComp target;
	int index;
	char response[64];
	FILE *fp;

	fp = fopen("ccomp.db","r+");
	if(fp == NULL){
		perror("fopen");
		exit(1);
	}
	flock(fileno(fp), LOCK_EX);

	index = atoi(argv[1]);

	fseek(fp, index * sizeof(CComp), SEEK_SET);
	fread(&target, sizeof(CComp), 1, fp);

	printf("Maker: %s\n", target.maker);
	if(requestValue("Maker")){
		getResponse(response);
		strcpy(target.maker, response);
	}
	printf("Model: %s\n", target.model);
	if(requestValue("Model")){
		getResponse(response);
		strcpy(target.model, response);
	}
	//strcpy(response, requestValue("Model"));
	printf("Year: %d\n", target.year);
	if(requestValue("Year")){
		printf("What value would you like to change it to?");
		scanf("%d", &target.year);
		//getResponse(response);
		//strcpy(target.maker, response);
	}
	//strcpy(response, requestValueChnage("Year"));
	printf("CPU: %s\n", target.cpu);
	if(requestValue("CPU")){
		getResponse(response);
		strcpy(target.cpu, response);
	}
	//strcpy(response, requestValueChnage("CPU"));
	printf("Desc: %s\n", target.desc);
	if(requestValue("Desciption")){
		getResponse(response);
		strcpy(target.desc, response);
	}
	//strcpy(response, requestValueChnage("Description"));
	
	fseek(fp, index * sizeof(CComp), SEEK_SET);
	fwrite(&target, sizeof(CComp), 1, fp);

	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	exit(0);
}
