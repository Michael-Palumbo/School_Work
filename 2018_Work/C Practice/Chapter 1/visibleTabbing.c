#include <stdio.h>

int main(void){
	char c;
	printf("Any tabs and backspaces will become visible for output, so be weary lol\n");
	while((c = getchar()) != EOF){
		if(c == '\t')
			printf("\\t");
		else if(c == '\\')
			printf("\\\\");
		else if(c == '\b')
			printf("\\b");
		else if(c == '\n')
			printf("\\n");
		else
			putchar(c);
	}
	printf("Thank you for your time\n");
	return 0;
}
