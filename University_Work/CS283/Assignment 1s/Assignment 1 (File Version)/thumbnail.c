#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){

	int WIDTH, HEIGHT, MAX;
	unsigned char ch;

	/* Reading in the file */
	
	if(argc == 1){
		printf("Please input an image to read!\n");
		return 1;
	}
	FILE *file = fopen(argv[1],"r");
	if(file == NULL){
		printf("Cannot find file!\n");
		return 2;
	}

	fscanf(file, "P5\n%d %d\n%d", &WIDTH, &HEIGHT, &MAX);
	
	int (*o_img)[WIDTH] = malloc(sizeof(int[HEIGHT][WIDTH]));

	/* Loading Original Image into a 2D Array */

	while(getc(file) != '\n'); 

	for(int row=0; row < HEIGHT; row++)
		for(int col = 0; col < WIDTH; col++){
			ch = getc(file);
			o_img[row][col] = ch;
		}
	
	fclose(file);

	/* Constructing a scaled down Image */

	int N_WIDTH = 200;
	int SCALE = WIDTH / N_WIDTH;
	int N_HEIGHT = HEIGHT/SCALE;

	int (*n_img)[N_WIDTH] = malloc(sizeof(int[N_HEIGHT][N_WIDTH]));

	/* Copying the content of the original image to the new image */

	for(int row=0; row < N_HEIGHT; row++)
		for(int col = 0; col < N_WIDTH; col++){
			n_img[row][col] = o_img[row*SCALE][col*SCALE];
		}

	/* Writing to a new file */

	char* new_name = malloc(strlen("thumbnail_") + strlen(argv[1]) + 1);
	strcpy(new_name,"thumbnail_");
	strcat(new_name,argv[1]);

	FILE *n_file = fopen(new_name, "w");
		
	fprintf(n_file, "P5\n%d %d\n%d", N_WIDTH, N_HEIGHT, MAX);

	for(int row=0; row < N_HEIGHT; row++)
		for(int col = 0; col < N_WIDTH; col++)
			fputc(n_img[row][col], n_file);
	
	fclose(n_file);	

	return 0;
}
