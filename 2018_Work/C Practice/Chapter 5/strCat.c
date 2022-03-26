#include <stdio.h>

void strCat(char*,char*);

int main(void){
	char str1[10] = "boy";
	char str2[10] = "dog";
	strCat(str2,str1);
	printf("Output: %s\n",str2);
	return 0;
}

void strCat(char *to, char *from){
	
	for( ; *to ; to++)
		;
//( *to++ != '\0') //we can omit '\0' becuase that's a value of 0, so we basically saying != 0 which is pointless

	while( (*to++ = *from++) ) //same here
		;
	
}
