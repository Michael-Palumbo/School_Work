#include <stdio.h>

#define MAXLENGTH 1000

int getLine(char[],int);
void rev(char[],int);
void swap(char*, char*);

int main(void){

	char length;
	char line[MAXLENGTH];

	while( (length = getLine(line,MAXLENGTH)) != 0 ){
		//printf("\nOriginal String: %s, with length: %d\n",line, length);
		rev(line,length);
		printf("%s\n",line);
	}
	printf("Finished\n");
	return 0;
}

int getLine(char line[], int max){
	char c, i;
	for(i = 0; i < max && (c = getchar()) != '\n' && c != EOF; i++)
		line[i] = c;
	
	if(i > 0) line[i] = '\0';

	return i;
}

void rev(char string[], int length){
	length--; //don't want to include '\0'
	for(int i = 0; i < length; i++, length--)
		swap(&string[i], &string[length]);
}

void swap(char *a, char *b){
	char temp = *a;
	*a = *b;
	*b = temp;
}

