#include <stdio.h>
#define ALLOCSIZE 20

char allocbuf[ALLOCSIZE];
char *allocp = allocbuf;

char *alloc(int size){
	if(ALLOCSIZE + allocbuf - allocp > size){
		allocp + size;
		return allocp - size;
	}
	return 0;
}

void afree(char *p){
	if(p >= allocbuf && p < allocbuf + ALLOCSIZE)
		allocp = p;
}
