#include <stdio.h>

#define MAXLENGTH 1000

void swap(char*,char*);
void reverse(char[]);
int len(char[]);
void itob(int,char[],int);

int main(void){
	int inp;
	int base;
	char output[MAXLENGTH];
	
	printf("Input: ");
	scanf("%d",&inp);
	printf("Base: ");
	scanf("%d",&base);
	
	itob(inp,output,base);
	
	printf("Output: %s\n",output);

	return 0;
}

void itob(int num, char set[], int base){
	int i = 0;

	do{
		set[i++] = (num % base) > 9 ? (num % base)-10 + 'a' : (num % base) + '0';
	}while( (num /= base) > 0 );

	set[i] = '\0';

	reverse(set);
}

void reverse(char set[]){
	for( int i = 0, j = len(set) - 1; i < j ; i++, j--)
		swap(set + i, set + j);
}

int len(char set[]){
	int i;
	for(i = 0 ; set[i] != '\0' ; i++)
		;
	return i;
}

void swap(char *a, char *b){
	char temp = *a;
	*a = *b;
	*b = temp;
}
