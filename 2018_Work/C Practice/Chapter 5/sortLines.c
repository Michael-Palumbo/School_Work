#include <stdio.h>
#include <stdlib.h>
#define MAXLINE 1000
#define MAXLINES 100

int getLines(char*[],int);
int getLine(char*,int);
void writeLines(char*[],int);
void copy(char*,char*);
int main(void){
	int length;
	char *allLines[MAXLINES];
	char line[MAXLINE];
	length = getLines(allLines,MAXLINES);
	printf("Test:%s\n",*allLines);
	writeLines(allLines,length);
	return 0;
}

int getLines(char *lineCollection[], int lim ){
	int i;
	char *p;
	char line[MAXLINE];

	for(i = 0;  getLine(line,MAXLINE) != 0 ; i++){
		p = (char*) malloc(MAXLINE * sizeof(char));
		copy(p,line);
		lineCollection[i] = p;
	}
	printf("Line Count: %d\n",i);
	return i;

}

int getLine(char *line, int lim){
	
	char *beginningPointer = line;
	char c;
	while( (c = getchar()) != '\n' && c != EOF )
		*line++ = c;
	//if(c == '\n')
	//	line--;
	*line = '\0';
	printf("Char count: %ld for line : \"%s\"\n",line-beginningPointer,beginningPointer);
	return line - beginningPointer;

}

void copy(char *dup, char *source){
	
	while( (*dup++ = *source++) != '\0' )
		;

}

void writeLines(char *lineptr[], int lim ){
	printf("Writing Lines:\n");
	for(int i = 0; i < lim ; i++)
		printf("%s\n",lineptr[i]);
	
}

void myQsort(){

}
