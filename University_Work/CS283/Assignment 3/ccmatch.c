#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>	
#include "cc.h"

int
main(int argc, char* argv[]){
	
	CComp comp;
	int index;
	char str[64];
	FILE *fp;

	if(argc != 2){
		perror("usage: ccmaker string");
		exit(2);
	}

	strcpy(str, argv[1]);

	fp = fopen("ccomp.db", "r+");
	if(fp == NULL){
		perror("fopen");
		exit(1);
	}
	flock(fileno(fp), LOCK_EX);

	fseek(fp, sizeof(CComp), SEEK_SET);
	
	for(index = 0; fread(&comp, sizeof(CComp), 1, fp) > 0; index++){
		if(strstr(comp.model, str) != NULL || strstr(comp.maker, str) != NULL || strstr(comp.desc, str) != NULL){
			printf("\n");
			printf("Maker: %s\n", comp.maker);
			printf("Model: %s\n", comp.model);
			printf("Year: %d\n", comp.year);
			printf("CPU: %s\n", comp.cpu);
			printf("Id: %d\n", comp.id);
			printf("Desc: %s\n", comp.desc);
			printf("----------------\n");
		}
	}

	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	
	exit(0);
}
