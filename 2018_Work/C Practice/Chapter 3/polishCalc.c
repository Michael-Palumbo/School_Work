#include <stdio.h>

#define NUMBER '0'
#define MAXLENGTH 100

double atof(char[]);
int getop(char[]);
int isdigit(int);
void push(double);
double pop(void);


double stack[MAXLENGTH];
int pointer = 0;

int main(void){
	int type;
	char word[MAXLENGTH];
	double temp; //we use in '-' and '/' since order matters
	while( (type = getop(word)) != EOF ){
		switch( type ){
			case NUMBER:
				push( atof(word) );
				break;
			case '+':
				push( pop() + pop() );
				break;
			case '*':
				push( pop() * pop() );
				break;
			case '-':
				temp = pop();
				push( pop() - temp );
				break;
			case '/':
				temp = pop();
				push( pop() / temp );
				break;
			case '\n':
				printf("The result: %f\n",pop());
				break;
			defualt:
				printf("ERROR COMMAND\n");
				break;
		}
	}

	return 0;
}

int getop(char s[]){

	int i, c;

	while( (c = getchar()) == ' ' || c == '\t') //clear out the leading spaces
		;
	
	s[0] = c; //c won't be a whitespace, could be a num or symbol

	if( !isdigit(c) && c != '.' ){ //c is a symbol
		s[1] = '\0';
		return c;
	}
	i = 0;
	if(isdigit(c)) // make sure c isn't a period
		while( isdigit( s[++i] = c = getchar() ) )
			;

	if(c == '.') //get decimal part
		while( isdigit( s[++i] = c = getchar() ) )
			;
	s[i] = '\0';  //we don't need to ++ since we know the current spot isn't a number

	return NUMBER;
}

int isdigit(int n){
	return n >= '0' && n <= '9';
}

double atof(char set[]){
	double val, power;
	int i, sign;
	
	for( i = 0 ; set[i] == ' ' ; i++)
		;

	sign = ( set[i] == '-' ) ? -1 : 1;

	if( set[i] == '+' || set[i] == '-')
		i++;

	for( val = 0; isdigit( set[i] ) ; i++ )
		val = 10.0 * val + ( set[i] - '0' );
	
	if( set[i] == '.' )
		i++;
	
	for( power = 1.0; isdigit( set[i] ) ; i++ ){
		val = 10.0 * val + ( set[i] - '0' );
		power *= 10;
	}
	
	return sign * val / power; 
}

void push(double n){
	stack[pointer++] = n;
}

double pop(){
	if(pointer > 0)
		return stack[--pointer];

	printf("ERROR\n");
	return 0.0;
}





