#include <stdio.h>
#include "calcHeader.h"

int getop(char s[]){
	int i, c;
	//printf("Wait what? with %s \n",s);
	while( (c = getch()) == ' ' || c == '\t')
		; //clearing out the leading spaces
	s[0] = c;
	//putchar(c);
	if( !isdigit(c) && c!= '.' ){
		s[1] = '\0';
		return c;
	}

	i = 0;
	if(isdigit(c)) //get integer part
		while( isdigit( s[++i] = c = getch() ) )
			;
	if(c == '.') //get decimal part
		while( isdigit( s[++i] = c = getch() ) )
			;
	
	s[i] = '\0';

	if(c != EOF)
		ungetch(c);

	return NUMBER;
}
