#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char* argv[]){

	FILE *fp;
	int index;
	char emptyStr[sizeof(CComp)];
	
	if( argc != 2 ){
		printf("usage: ccdel index\n");
		exit(2);
	}

	fp = fopen("ccomp.db", "r+");
	if(fp == NULL){
		perror("fopen");
		exit(1);	
	}
	flock(fileno(fp), LOCK_EX);
	index = atoi(argv[1]);
	fseek(fp, index * sizeof(CComp), SEEK_SET);
	fwrite(&emptyStr, sizeof(CComp), 1, fp);

	flock(fileno(fp), LOCK_UN);
	fclose(fp);

	exit(0);
}

