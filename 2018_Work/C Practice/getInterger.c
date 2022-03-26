#include <stdio.h>

int getInt(int*);
int isdigit(int);

int main(void){ //Not the best example
	int num = 0;
	int total = 0;
	while( getInt(&num) != EOF )
		total += num;
	printf("The total is %d\nDone",total);
	return 0;
}

int getInt(int *num){ //basically the conversion, but getting chars and affecting num
	int c, sign;

	while( (c = getchar()) == ' ' || c =='\n')
		;

	if( !isdigit(c) && c !=EOF && c != '+' && c !='-' ){
		 //ungetch(); //c is not a integer
		 return 0;
	}

	sign = (c == '-') ? -1 : 1;
	if(c == '+' || c == '-')
		c = getchar();

	for( *num = 0 ; isdigit(c) ; c = getchar() )
		*num = 10 * *num + (c - '0');

	*num *= sign;
	printf("Leaving num: %d\n",*num);
	//if(c == EOF)
	//	return EOF;
	
	return c;
}

int isdigit(int given){
	return given >= '0' && given <= '9';
}


