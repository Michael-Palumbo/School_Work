#include <stdio.h>
#include <ctype.h>
#define MAXLENGTH 100

void expand(char[],char[]);
int getLine(char[],int);

int main(void){
	char s1[MAXLENGTH];
	char s2[MAXLENGTH];

	getLine(s1,MAXLENGTH);
	
	expand(s1,s2);
	
	printf("Original String: %s\nExpanded String: %s\n",s1,s2);

	return 0;
}

int getLine(char s1[], int lim){
	int i;
	for( i = 0 ; i < lim && (s1[i] = getchar()) != '\n' && s1[i] != EOF ; i++)
		;
	s1[i] = '\0';
	return i;
}
void expand(char s1[],char s2[]){
	char c;
	int i = 0, j = 0; //i is index of s1, and j is index of s2
	
	while( (c = s1[i]) != '\0'){
		
		char nextC = s1[i+1];
		if(nextC == '-'){
			char thirdC = s1[i+2];
			if(
			( isdigit(c) && isdigit(thirdC) ) ||
			( islower(c) && islower(thirdC) ) ||
			( isupper(c) && isupper(thirdC) )
			) {
				if(c < thirdC)
					while( c <= thirdC ){
						s2[j++] = c;
						c++;
					}
				else
					while( c >= thirdC ){
						s2[j++] = c;
						c--;
					}
				//i += (s1[i+3] == '-') ? (1,j--) : 3;//anticpating a-b-c;
				if(s1[i+3] == '-'){
					i+=2;
					j--;
				}else
					i += 3;
			}
			else
				s2[j++] = s1[i++];
		}else
			s2[j++] = s1[i++];
	}
	s2[j] = '\0';
}
