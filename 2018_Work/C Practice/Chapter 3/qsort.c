#include <stdio.h>

void qsort(char[],int,int);
void swap(char[],int,int);

int main(void){
	char set[] = {'Z','A','B','F','M','C','D'};
	qsort(set,0,6);
	printf("%s\n",set);
	return 0;
}

void qsort(char set[], int left, int right){
	int i, last;
	if(left >= right)
		return;
	
	swap(set, left, (left+right)/2);
	last = left;
	for(i = left+1 ; i <= right; i++)
		if( set[i] < set[left] )
			swap(set,++last,i);

	swap(set,left,last);
	qsort(set,left,last-1);
	qsort(set,last+1,right);
}

void swap(char s[], int p1, int p2){
	int temp = s[p1];
	s[p1] = s[p2];
	s[p2] = temp;
}
