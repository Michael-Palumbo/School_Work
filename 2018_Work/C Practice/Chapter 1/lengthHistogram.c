#include <stdio.h>

#define MAX 1000
#define max(a,b) a >= b ? a : b

int main(void){

	int lengths[MAX];
	int count = 0, max_length = 0;
	char c;
	float NORMAL = 1.0f;
	
	for(int i = 0 ; i < MAX ; i++)
		lengths[i] = 0;

	while( (c = getchar()) != EOF){
		if((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
			count++;
		else{
			if(count == 0) continue;
			if(count >= MAX) count = MAX - 1;
			lengths[count]++;
			count = 0;
		}
	}

	for(int i = 0 ; i < MAX ; i++)
		max_length = max(max_length,lengths[i]);
	
	if(max_length > 50) NORMAL = max_length*1.0f / 50;
	
	printf("Normal: %f, max_length: %d\n",NORMAL,max_length);

	for(int i = 0 ; i < MAX ; i++){
		if(lengths[i] != 0){
			printf("Words with length %3d appeared %6d time(s)",i,lengths[i]);
			for(int ii = 0; ii < (int)(lengths[i] / NORMAL); ii++)
				printf("#");
			printf("\n");
		}
	}
	printf("Finished\n");
	return 0;
} 
