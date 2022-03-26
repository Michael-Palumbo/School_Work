#include <stdio.h>

#define MAXLENGTH 1000

void sqeeze(char[],char);
void sqeezePhrase(char[],char[]);
int main(void){
	char remove = 's';
	char removeSet[MAXLENGTH] = "am";
	char test[MAXLENGTH] = "aaanimals are dumb asses";

	printf("Orginal: %s, removing: %c\n",test,remove);
	sqeeze(test,remove);
	printf("Changed: %s\n",test);

	printf("Orginal: %s, removing: %s\n",test,removeSet);
	sqeezePhrase(test,removeSet);
	printf("Changed: %s\n",test);

	return 0;
}

void sqeeze(char target[], char set){
	int j;
	for( int i = j = 0; target[i] != '\0' ; i++){
		if(target[i] != set){
			target[j] = target[i]; //Also could be target[j++]
			j++;
		}
	}
	target[j] = '\0';
}

//Alternative approach, just use sqeeze for each character in set
void sqeezePhrase(char target[], char set[]){
	int j;
	for(int i = j = 0; target[i] != '\0'; i++){
		int contains = 0; //0 is false
		for( int ii = 0; set[ii] != '\0' ; ii++){
			if(target[i] == set[ii]){
				contains = 1;
				break;
			}
		}
		if(!contains) target[j++] = target[i];
	}
	target[j] = '\0';
}
