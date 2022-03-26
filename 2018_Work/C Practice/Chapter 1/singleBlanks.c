#include <stdio.h>

int main(void){
	char c, onBlank = 0;
	printf("Enter Some Shit with multiple spaces and we'll shorten them for you\n");
	while((c = getchar())!= EOF){
		if(c == ' ' ){
			if(!onBlank){
				onBlank = 1;
				putchar(c);
			}
		}else{
			onBlank = 0;
			putchar(c);
		}
	}
	printf("\n");
	return 0;
}
