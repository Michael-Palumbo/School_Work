#include <stdio.h>

#define MAXLENGTH 1000

int atoi(char[]);
int getWord(char[]);

int main(void){
	int num, length;
	char word[MAXLENGTH];
	
	while( (length = getWord(word)) != 0){
		num = atoi(word);
		printf("Result: %d\n",num);
	}		
	return 0;
}

int getWord(char word[]){
	int c, i;
	for(i = 0; (c = getchar()) != ' ' && c != '\n' && c != EOF; i++)
		word[i] = c;
	word[i] = '\0';
	return i;
}

int atoi(char inp[]){
	int num;
	num = 0;

	for( int i = 0; inp[i] >= '0' && inp[i] <= '9' ; i++)
		num = 10 * num + (inp[i] - '0');
	
	return num;

}
