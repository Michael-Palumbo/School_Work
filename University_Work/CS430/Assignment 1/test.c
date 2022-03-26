#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int
main(int argc, char* argv[]){
	printf("%c\n", argv[1][0]);
	printf("%c\n", argv[1][1]);
}