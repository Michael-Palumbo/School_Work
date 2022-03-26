#include <stdio.h>
#include "calcHeader.h"

static double stack[MAXLENGTH];
static int stackPointer = 0;

void push(double x){
	if(stackPointer < MAXLENGTH)
		stack[stackPointer++] = x;
	else
		printf("ERROR, FULL STACK");
}

double pop(){
	if(stackPointer > 0)
		return stack[--stackPointer];
		
	printf("ERROR, EMPTY STACK");
	return 0;
}
