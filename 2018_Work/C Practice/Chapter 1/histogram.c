#include <ctype.h>
#include <stdio.h>
int main(void){
	
	char c;
	long int alpha[26]; // a is 97

	for(int i  = 0 ;  i < 26 ; i++)
		alpha[i] = 0;

	printf("Your Input:\n");
	while((c = getchar()) != EOF){
		if(tolower(c) >= 'a' && tolower(c) <= 'z')
			alpha[tolower(c)- 'a']++;
		putchar(c);
	}
	printf("\nMost Common Letters:\n");
	for(int i = 0 ; i<26 ; i++){
		printf("%c:%ld\t",i+'a',alpha[i]);
	//	for(int ii = 0; ii < alpha[i] ; ii++)
	//		printf("#");
	//	printf("\n");
	}
	printf("\nFinished\n");
	return 0;
}
	 
