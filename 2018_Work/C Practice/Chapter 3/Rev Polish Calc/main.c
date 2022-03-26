#include <stdio.h>
#include "calcHeader.h"

extern double stack[];
extern int stackPointer;

int main(void){
	double temp;
	char word[1000];	
	int op;
	//printf("Enter shit here\n");
	while( (op = getop(word)) != EOF){
		//printf("Reached switch");
		switch(op){
			case NUMBER:
				push(atof(word));
				break;
			case '+':
				push(pop() + pop());
				break;
			case '*':
				push(pop() * pop());
				break;
			case '-':
				temp = pop();
				push(pop() - temp);
				break;
			case '/':
				temp = pop();
				push(pop() / temp);
				break;
			case '\n':
				printf("%f\n",pop());
				break;
		}
	}

	return 0;
}

