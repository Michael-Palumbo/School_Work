#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char* argv[]){
	
	CComp comp;
	int index;
	int yearstart, yearend;
	FILE *fp;

	if(argc != 3){
		perror("usage: ccyear start_year end_year");
		exit(2);
	}

	yearstart = atoi(argv[1]);
	yearend = atoi(argv[2]);

	fp = fopen("ccomp.db", "r+");
	if(fp == NULL){
		perror("fopen");
		exit(1);
	}
	flock(fileno(fp), LOCK_EX);

	fseek(fp, sizeof(CComp), SEEK_SET);
	
	for(index = 0; fread(&comp, sizeof(CComp), 1, fp) > 0; index++){
		if(comp.year >= yearstart && comp.year <= yearend){
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
