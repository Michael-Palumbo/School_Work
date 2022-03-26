#include <stdio.h>

#define MAXLENGTH 1000

int find(char[],char[]);

int main(void){
	char test[MAXLENGTH] = "I want to find the word";
	char word[MAXLENGTH] = "to";
	int found;

	found = find(test,word);

	printf("Input: %s\nFound: %s at %d\n",test,word,found);

	return 0;
}

int find(char target[], char finding[]){
	for(int i = 0 ; target[i] != '\0'; i++)
		for( int s = i, e = 0; finding[e] != '\0' && target[s] != '\0' ; s++,e++){
			if(target[s] != finding[e])
				break;
			if(finding[e+1] == '\0') return i; //probably not the most efficient way
		}
	return -1;
}
