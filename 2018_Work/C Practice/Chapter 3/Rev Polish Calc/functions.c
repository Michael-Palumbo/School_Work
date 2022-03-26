#include <stdio.h>
#include "calcHeader.h"

int isdigit(int n){
	return n >= '0' && n <= '9';
}

double atof(char set[]){
	double val, power;
	int i, sign;
	
	//skipping leading spaces
	for(i = 0 ;  set[i] == ' ' ; i++)
		;
	//check to see if negative
	sign = (set[i] == '-') ? -1 : 1;

	//move past negative (or positive, just incase)
	if(set[i] == '+' || set[i] == '-')
		i++;

	//get integer portion
	for(val = 0; isdigit(set[i]) ; i++)
		val = 10 * val + (set[i]-'0');

	//check to see if there is decimal portion, if so, load that too
	if(set[i] == '.')
		i++;
	
	for(power = 1.0 ; isdigit(set[i]) ; i++, power *= 10)
		val = 10 * val + (set[i]-'0');
	
	return sign * val / power;
}
