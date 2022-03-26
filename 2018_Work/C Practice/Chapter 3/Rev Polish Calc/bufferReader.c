#include <stdio.h>
#include "calcHeader.h"

static char buf[MAXLENGTH];
static int bufferPointer = 0;

int getch(){
	
	//if( bufferPointer > 0);
	//	return buf[--bufferPointer];
	//return getchar();
	return (bufferPointer > 0) ? buf[--bufferPointer] : getchar();
}

void ungetch(char c){

	if( bufferPointer < MAXLENGTH )
		buf[bufferPointer++] = c;
	else
		printf("ERROR, BUFFER READER IS FULL");
}
