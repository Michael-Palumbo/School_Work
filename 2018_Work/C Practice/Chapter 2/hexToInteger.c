#include <stdio.h>

#define MAXLENGTH 100

int getWord(char[]);
int htoi(char[]);
char lower(char);

int main(void){
	char word[MAXLENGTH];
	int num, length;
	
	while( (length = getWord(word)) != 0 ){
		num = htoi(word);
		printf("Result: %d\n",num);
	}
	return 0;
}

int getWord(char word[]){
	int c, i;
	printf("Hex: ");
	for( i = 0; (c = getchar()) != ' ' && c != '\n' && c != EOF ; i++)
		word[i] = c;
	
	word[i] = '\0';
	//printf("The word: %s, length of word is %d\n",word,i);
	return i;
}

int htoi(char hex[]){
	int num;
	num = 0;

	for( int i = 0; (hex[i] >= '0' && hex[i] <= '9') || (lower(hex[i]) >= 'a' && lower(hex[i]) <= 'f') ; i++)
		num = 16* num + ( (hex[i] >= '0' && hex[i] <= '9') ? hex[i] - '0' : lower(hex[i]) - 'a' + 10  );

	return num;
}
char lower(char c){
	
	return (c >= 'A' && c <= 'Z') ? c + 'a' - 'A' : c;
}
