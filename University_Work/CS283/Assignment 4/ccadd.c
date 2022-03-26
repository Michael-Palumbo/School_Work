#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/sysmacros.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[])
{
	CComp new;
	FILE *fp;

	if(argc != 7) {
		fprintf(stderr, "Usage: ccadd id maker model year cpu desc\n");
		exit(1);
	}
	
	if(strcmp(argv[1], "-a") == 0 ){
		//printf("-a reached\n");
		struct stat ccstat;
		if(stat("ccomp.db", &ccstat) < 0){
			perror("stat");
			exit(2);
		}
		new.id = (ccstat.st_size / sizeof(CComp));
	}
	else{
		//printf("non -a reached\n");
		new.id = atoi(argv[1]);
	}
	strncpy(new.maker, argv[2], Nmaker-1);
	new.maker[Nmaker-1] = '\0';
	strncpy(new.model, argv[3], Nmodel-1);
	new.model[Nmodel-1] = '\0';
	new.year = atoi(argv[4]);
	strncpy(new.cpu, argv[5], Ncpu-1);
	new.cpu[Ncpu-1] = '\0';
	strncpy(new.desc, argv[6], Ndesc-1);
	new.desc[Ndesc-1] = '\0';


	fp = fopen("ccomp.db", "r+");
	if(fp == NULL) {
		perror("fopen");
		exit(2);
	}
	flock(fileno(fp), LOCK_EX);
	fseek(fp, new.id * sizeof(CComp), SEEK_SET);
	fwrite(&new, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	exit(0);
}
