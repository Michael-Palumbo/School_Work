#include <stdio.h>
#include <stdlib.h>

int main(){

	int WIDTH, HEIGHT, MAX, N_WIDTH, N_HEIGHT, SCALE;
	char *o_img, *n_img; 

	scanf("P5\n%d %d\n%d", &WIDTH, &HEIGHT, &MAX);
	
	o_img = malloc(sizeof(char[HEIGHT * WIDTH]));

	/* Loading Original Image into a 2D Array */

	while(getchar() != '\n'); 

	fread(o_img, sizeof(char), HEIGHT * WIDTH, stdin);

	/* Constructing a scaled down Image */

	SCALE = WIDTH / 200;
	N_HEIGHT = HEIGHT/SCALE;
	N_WIDTH = WIDTH/SCALE;

	n_img = malloc(sizeof(char[N_HEIGHT * N_WIDTH]));

	/* Copying the content of the original image to the new image */

	for(int row=0; row < N_HEIGHT; row++)
		for(int col = 0; col < N_WIDTH; col++){
			*(n_img + N_WIDTH * row + col) = *(o_img + WIDTH *(row*SCALE) + (col*SCALE) );
		}	

	/* Writing to a new file */

	printf("P5\n%d %d\n%d\n", N_WIDTH, N_HEIGHT, MAX);

	fwrite(n_img, sizeof(char), N_WIDTH * N_HEIGHT, stdout);

	exit(0);
}
