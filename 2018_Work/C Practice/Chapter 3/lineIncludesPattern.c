#include <stdio.h>

#define MAXLENGTH 1000

int getLine(char[],int);
int indexof(char[],char[]);

int main(void){
	char pattern[] = "is";
	char line[MAXLENGTH];
	int found = 0;

	while( getLine(line,MAXLENGTH) > 0 )
		if( indexof(line,pattern) != -1){
			printf("%s",line);
			found++;
		}
	
	printf("\n%d\n",found);

	return 0;
}

int getLine(char line[],int lim){
	int i;
	char c;

	for(i = 0 ; i < lim && (c = getchar()) != '\n' && c != EOF ; i++)
		line[i] = c;
	
	if( c == '\n' ) line[i++] = '\n';

	line[i] = '\0';

	return i;
}

int indexof(char line[], char pattern[]){
	int i,j,k;
	for( i = 0 ; line[i] != '\0' ; i++){
		for ( j = i, k = 0; pattern[k] != '\0' && line[j] == pattern[k] ; j++, k++ )
			; //Walk through pattern, increasing k for each match, if k reached end we know it matches
		if(k > 0 && pattern[k] == '\0')
			return i;
	}

	return -1;
}
