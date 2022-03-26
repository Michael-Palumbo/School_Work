#include <stdio.h>

void swap(char*,char*);
void qsort(char*,char*);

int main(void){
	char temp[] = {'z','b','a','m','g', '\0'};
	char *start = temp;
	char *last = start + 5;
	qsort(start,last);
	printf("List: %s",temp);
	return 0;
}

void qsort(char *left, char *right){

	if( left > right ) return;

	swap(left, (left+right)/2);

	char *last = left;
	
	for(char *i = left+1; i <= right; i++)
		if( *i < *left )
			swap(++last,i);
	
	swap(left,last);
	qsort(left,last);
	qsort(last+1,right);

 /*
	for (int i = left +1; i<= right; i++)
		if (set[i] < set[left])
			swap(set, ++last, i)

	swap(set, left, last)
	qsort(l,last) last+1 right
  */

}
void swap(char *a, char *b){
	char temp = &a;
	&a = &b;
	&b = temp;
}
