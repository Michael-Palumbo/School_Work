#include <stdio.h>

#define MAXLENGTH 1000

int len(char[]);
void swap(char*,char*);
void reverse(char[]);
void itoa(int,char[]);

int main(void){
	int num;
	scanf("%d",&num);
	char test[MAXLENGTH];
	
	itoa(num,test);

	printf("Num: %d\nString: %s\n",num,test);

	return 0;
}

void itoa(int num, char set[]){
	
	int i, sign;
	//Added function for negatives
	i = 0;

	if( (sign = num) < 0 )
		num *= -1;

	do{
		set[i++] = (num % 10) + '0';
	}while( (num /= 10) > 0 && i < MAXLENGTH);
	
	if(sign < 0) set[i++] = '-';

	set[i++] = '\0';
	reverse(set);
}

void reverse(char set[]){
	
	for(int i = 0, j = len(set)-1; i < j; i++, j--)
		swap(set + i,set + j); //swap(&set[i],&set[j]);

}

int len(char set[]){
	int i = 0;
	while(set[i++] != '\0')
		;
	return i-1; //i was still incremented, so we gotta undo
}

void swap(char *a, char *b){
	char temp = *a;
	*a = *b;
	*b = temp;
}
