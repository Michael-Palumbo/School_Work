#include <stdio.h>

int main(void){
	char s[] = {'A','C','E'};
	char *p = s;
	printf("1st: %c\n",++(*p));//B
	printf("2nd: %c\n",*++p); //C
	p++;
	printf("3rd: %c\n",*p); //E
	return 0;
}
