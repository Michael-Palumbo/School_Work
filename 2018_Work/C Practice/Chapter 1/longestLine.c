#include <stdio.h>

#define MAXLENGTH 1000

int getLine(char[]);
void copy(char[], char[]); 

int main(void){

	int lineLength, maxLineLength = 0;
	char currentLine[MAXLENGTH];
	char maxLine[MAXLENGTH];
	
	while( (lineLength = getLine(currentLine)) != 0 ){
		if(lineLength > maxLineLength){
			maxLineLength = lineLength;
			copy(maxLine,currentLine);
		}
	}
	printf("\nPre-knowledge: maxlineLength: %d\n",maxLineLength);
	
	//for(int i = 0; i < maxLineLength ; i++)
	//	printf("%c",maxLine[i]);

	printf("%s\n",maxLine);
	
	//printf("*\n");

	printf("Finished\n");
}

int getLine(char lineRef[]){
	char c, i;
	for( i = 0; i < MAXLENGTH && (c = getchar()) != '\n' && c != EOF; i++)
		lineRef[i] = c;
	lineRef[i] = '\0';
	return i;
	
}

void copy(char dup[], char orginal[]){

	for(int i = 0 ; (dup[i] = orginal[i]) != '\0' ; i++);

}
