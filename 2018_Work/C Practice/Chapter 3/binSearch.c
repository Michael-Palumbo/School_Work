#include <stdio.h>

int binSearch(int, int[], int);

int main(void){
	int test[] = {5,10,13,20,22,25,34,42,50,63,70,81,99,102};
	
	int found= binSearch(99,test,13);

	printf("Found %d, at %d\n",99,found);

	return 0;
}

int binSearch(int search, int set[], int length){
	int low,mid,high;
	
	low = 0;
	high = length-1;
	while(low <= high){
		mid = (low+high)/2;
		if(search < set[mid])
			high = mid-1;
		else if(search > set[mid])
			low = mid+1;
		else
			return mid;
	}
	return -1;
}
