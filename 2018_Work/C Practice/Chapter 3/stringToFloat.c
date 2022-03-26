#include <stdio.h>

#define MAXLENGTH 1000
#define isdigit(n) n >= '0' && n <= '9'

int getLine(char[], int);
double atof(char[]);

int main(void){
	char test[MAXLENGTH]; 
	double ans;
	
	while( getLine(test,MAXLENGTH) > 0 ){
		ans += atof(test);
		printf("Total: %f\n",ans);
	}

	return 0;
}

int getLine(char line[], int lim){
	int c,i;
	i = 0;
	while( i < lim && (c = getchar()) != '\n' && c != EOF)
		line[i++] = c; //structured like for, but for is for iterating
	if(c == '\n') line[i++] = c;
	line[i] = '\0';
	return i;
}

double atof(char s[]){
	int i, sign;
	double val, power;
	
	for(i = 0 ; s[i] == ' '; i++)
		;

	sign = (s[i] == '-') ? -1 : 1;

	if(s[i] == '+' || s[i] == '-') i++;

	for(val = 0; isdigit(s[i]) ; i++)
		val = 10.0 * val + ( s[i] - '0' );
	
	if(s[i] == '.') i++;
	
	for(power = 1; isdigit(s[i]) ; i++)
		val = 10.0 * val + ( s[i] - '0' ), power *= 10.0;

	return sign * val / power;
}

