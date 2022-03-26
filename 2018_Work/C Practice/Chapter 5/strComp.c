#include <stdio.h>

//	Not comparison between the array verion and pointer versions

int strComp(char[],char[]);
int strCompP(char*,char*);

int main(void){
	char s1[10] = "abc";
	char s2[10] = "abc";
	int comp = strCompP(s1,s2);
	if( comp < 0 )
		printf("%s is less than %s",s1,s2);
	else if( comp > 0 )
		printf("%s is greater than %s",s1,s2);
	else
		printf("%s is equal to %s",s1,s2);
	putchar('\n');
	return 0;
}
// < 0 if s < t, 0 if s == t, >0 if s > t
int strComp(char s1[], char s2[]){
	int i;
	for( i = 0; s1[i] == s2[i]; i++)
		if(s1[i] == '\0') //one reached the end, and we already know they equal
			return 0;
	return s1[i] - s2[i];
}

int strCompP(char *s1, char *s2){

	for ( ; *s1 == *s2 ; s1++, s2++ )
		if(*s1 == '\0')
			return 0;
	
	return *s1 - *s2;
}
