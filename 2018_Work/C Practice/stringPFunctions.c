#include <stdio.h>

int strlength(char[]);
void strcopy(char*,char*);

int main(void){
	char str[] = "This is a temp";
	printf("The of length of \"%s\" is %d\n",str,strlength(str));
	char str2[20];
	strcopy(str2,str);
	printf("String 2 is now %s\n",str2);
	return 0;
}

int strlength(char *s){
	int i;
	for( i = 0 ; *s != '\0'; i++, s++)
		;
	return i;
}

void strcopy(char *change, char *org){
	while( ( *change++ = *org++ ) != '\0' ) //same as change[i++]
		;
}
