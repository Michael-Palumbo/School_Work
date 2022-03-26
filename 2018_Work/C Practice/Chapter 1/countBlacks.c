#include<stdio.h>

int main(){
	
	char c;
	int count = 0;
	while((c = getchar())!=EOF){
		if(c == '\t' || c == ' ' || c == '\n')
			count++;
	}
	printf("\nThere were %d amount of tabs\n",count);
	return 0;
}
