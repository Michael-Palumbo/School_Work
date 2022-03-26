#include <stdio.h>

#define MAXLENGTH 1000

int getLineP(char*,int);

int main(void){
	char line[MAXLENGTH];
	int length;

	while( (length = getLineP(line,MAXLENGTH)) != 0 )
		printf("\"%s\" is %d character(s) long\n",line,length);

	return 0;
}

int getLineP(char *line, int lim){
	char *refToBigining = line;
	int c;
	while( (line - refToBigining) < lim && (c = getchar()) != '\n' && c != EOF )
		*line++ = c;
	*line = '\0';
	return line - refToBigining;
}
