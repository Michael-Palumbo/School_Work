#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>

#define DEG2RAD(x) (x*M_PI/180)
#define INSIDE 0 //0000
#define LEFT 1   //0001
#define RIGHT 2  //0010
#define BOTTOM 4 //0100
#define TOP 8    //1000


/* CONSTANTS */
int worldXMin = 0, worldXMax = 499, worldYMin = 0, worldYMax = 499;
int width, height ;
char* fileName;

float scaleFactor = 1.0f, rotation = 0.0f;
int translateX = 0, translateY = 0; 


/* LINE KNOWLEDGE */

typedef struct Line Line;

struct Line{
	int x1,y1,x2,y2;
};

typedef struct LineArray LineArray;

struct LineArray{
	Line *line;
	LineArray * next;
};

LineArray *lines;

/*PROTOTYPES*/

void printArray();
void addLine(Line*);
void removeLine(LineArray*);
void cleanLineArray(LineArray);

void readPS();

void swap(int *, int *);

void draw(char *);
void drawPoint(int, int);

void scaleLines();
void rotateLines();
void translateLines();
void clipLines();
int getCode(int, int);

void printPixels(char *);

void processArgs(int, char*[]);


int
main(int argc, char* argv[]){

	fileName = malloc(sizeof(char) * 64);
	strcpy(fileName, "hw1.ps");

	processArgs(argc, argv);

	height = worldYMax - worldYMin;
	width = worldXMax - worldXMin;

	readPS(); //we now have lines contain the lines struct for all the lines

	char * pixels = malloc(sizeof(char[height * width]));

	//Trasnform the lines
	scaleLines();
	rotateLines();
	translateLines();

	//Clip the lines
	clipLines();

	//Draw the lines on the 2d array
	draw(pixels);

	// Print the contents
	printPixels(pixels);
	printArray();

	free(pixels);
	free(lines);
	return 0;
}


void
readPS(){
	
	char *BUF = malloc(sizeof(char) * 124); //Read in input
	char *type = malloc(sizeof(char) * 32); //Not really used yet

	FILE *f = fopen(fileName,"r");


	//Ignore all text until %%%BEGIN is reached
	while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%BEGIN\n",8));


	//Read till %%%END is reached
	while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%END\n",6)){
		if(strlen(BUF) > 4){
			// printf("%s\n",BUF);
			Line *tempLine = (Line *)malloc(sizeof(Line));
			sscanf(BUF, "%d %d %d %d %s", &tempLine->x1, &tempLine->y1, &tempLine->x2, &tempLine->y2, type);
			addLine(tempLine);
		} 
	}

	free(BUF);
	free(type);
	
}

/* O(n) */
void
addLine(Line *line){
	
	//First time we call addLine
	if(lines == NULL){
		lines = (LineArray *)malloc(sizeof(LineArray));
		lines->line = line;
		return;
	}



	//Get to the last time we added a value;
	LineArray *current = lines;
	while(current->next != NULL)
		current = current->next;

	//current->next == NULL so give it a location, then add a line to it
	current->next = (LineArray *)malloc(sizeof(LineArray));
	current->next->line = line;

	return;
}

void
removeLine(LineArray* tLine){
	LineArray *current = lines;
	while(current->next != tLine)
		current = current->next;

	//free(tLine); //breaks my for loop, i know why, its late and I don't have time to restructure it
	current->next = current->next->next;
}

void
printArray(){
	fprintf(stderr, "LINKEDLIST CHECKER [] \n");
	for(LineArray *lineA = lines; lineA != NULL; lineA = lineA->next){
		Line *tempLine = lineA->line;
		fprintf(stderr, "%d %d %d %d\n", tempLine->x1, tempLine->y1, tempLine->x2, tempLine->y2);
	}
}

void
draw(char * pixels){

	//Make everything white
	for (int i=0; i<height; i++){
		for (int j=0; j<width; j++){
			*(pixels + i * width + j) = '0';
		}	
    }

    //Loop through my linked list, use DDA to draw out each line
	for (LineArray *tLine = lines; tLine != NULL; tLine = tLine->next){
		int x1 = tLine->line->x1 - worldXMin;
		int y1 = tLine->line->y1 - worldYMin;
		int x2 = tLine->line->x2 - worldXMin;
		int y2 = tLine->line->y2 - worldYMin;
		
		char steep = (abs(y2 - y1) > abs(x2 - x1)) ? 1 : 0;

		//Slope greater than 1
		if(steep){
			swap(&x1, &y1);
			swap(&x2, &y2);
		}

		// Line heads left, swap points
		if(x1 > x2){
			swap(&x1, &x2);
			swap(&y1, &y2);
		}

		int dErr = abs(y2 - y1);
		int yStep = y1 > y2 ? -1 : 1;
		int dX = x2 - x1;

		int err = dX >> 1;

		int y = y1;

		for(int x = x1; x < x2; x++){
			if(steep)
				*((pixels+x*width)+y) = '1'; //drawPoint(y,x);
			else
				*((pixels+y*width)+x) = '1'; //drawPoint(x,y);
			err -= dErr;
			if(err < 0){
				y += yStep;
				err += dX;
			}
		}
	}
}

void
swap(int * a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

void
printPixels(char * pixels){
	printf("P1\n");
	printf("# test.pbm\n");
	printf("%d %d\n", width, height);

	for (int i=0; i<height; i++){
		for (int j=0; j<width; j++)
			printf("%c ", *(pixels + i * width + j));
		printf("\n");
	}
 
	// They need spaces so this doesn't work :(
	// fwrite(pixels, sizeof(char), width * height, stdout);

   	printf("\n");
}

void
scaleLines(){
	for (LineArray *tLine = lines; tLine != NULL; tLine = tLine->next){
		Line *line = tLine->line;
		line->x1 = (int) (line->x1 * scaleFactor);
		line->y1 = (int) (line->y1 * scaleFactor);
		line->x2 = (int) (line->x2 * scaleFactor);
		line->y2 = (int) (line->y2 * scaleFactor);

	}
}

void
rotateLines(){
	for (LineArray *tLine = lines; tLine != NULL; tLine = tLine->next){
		Line *line = tLine->line;
		int temp_x1 = (int) (line->x1 * cos(rotation) - (line->y1 * sin(rotation)));
		int temp_y1 = (int) (line->x1 * sin(rotation) + (line->y1 * cos(rotation)));
		int temp_x2 = (int) (line->x2 * cos(rotation) - (line->y2 * sin(rotation)));
		int temp_y2 = (int) (line->x2 * sin(rotation) + (line->y2 * cos(rotation)));
		line->x1 = temp_x1;
		line->y1 = temp_y1;
		line->x2 = temp_x2;
		line->y2 = temp_y2;

	}
}

void
translateLines(){
	for (LineArray *tLine = lines; tLine != NULL; tLine = tLine->next){
		Line *line = tLine->line;
		line->x1 = line->x1 + translateX;
		line->y1 = line->y1 + translateY;
		line->x2 = line->x2 + translateX;
		line->y2 = line->y2 + translateY;
	}
}

int
getCode(int x, int y){
	int code = INSIDE;
    	
	//Setting bits
	if (x < worldXMin)
		code += LEFT;
				
	if(x > worldXMax)
        code += RIGHT;
	
	if(y > worldYMax)
		code += TOP;
	
	if(y < worldYMin)
		code += BOTTOM;
		
	return code;
}

void
clipLines(){
	for (LineArray *tLine = lines; tLine != NULL; tLine = tLine->next){
		int x1 = tLine->line->x1;
		int y1 = tLine->line->y1;
		int x2 = tLine->line->x2;
		int y2 = tLine->line->y2;

		int code1 = getCode(x1, y1); 		
    	int code2 = getCode(x2, y2);

		char accept = 0;
        
            
		while(1){
			//Line is completely in view
			if((code1 | code2) == 0){
				accept = 1;
				break;
			}
			
			//Line is compeletly invisible
			else if((code1 & code2) != 0){
				removeLine(tLine);
				break;
			}
			//Line clipping
			else{
				int x = 0,y = 0;
				
				int codeout = (code1 >= 1) ? code1 : code2;

				//Line intersects top of window
				if((codeout & TOP) >= 1){
					x = x1 + (x2 - x1) * (worldYMax - y1) / (y2 - y1);
					y = worldYMax;
				}
				//Line intersects bottom of window
				else if((codeout & BOTTOM) >= 1){
					x = x1 + (x2 - x1) * (worldYMin - y1) / (y2 - y1);
					y = worldYMin;
				}
				//Line intersects right of window
				else if((codeout & RIGHT) >= 1){
					y = y1 + (y2 - y1) * (worldXMax - x1) / (x2 - x1);
					x = worldXMax;
				}
				//Line intersects left of window
				else if((codeout & LEFT) >= 1){
					y = y1 + (y2 - y1) * (worldXMin - x1) / (x2 - x1);
					x = worldXMin;
				}
				
				if(codeout == code1){
					x1 = x;
					y1 = y;
					code1 = getCode(x1, y1);
				}else{
					x2 = x;
					y2 = y;
					code2 = getCode(x2, y2);
				}
			}
		}
    	if(accept){
    		tLine->line->x1 = x1;
			tLine->line->y1 = y1;
			tLine->line->x2 = x2;
			tLine->line->y2 = y2;
    	}	
	}
}

void
processArgs(int argc, char*argv[]){
	for(int i = 1; i < argc; i+=2){
		if(argv[i][0] == '-'){
			switch(argv[i][1]){
				case 'f':
					strcpy(fileName, argv[i+1]);
					break;
				case 's':
					scaleFactor = atof(argv[i+1]);
					break;
				case 'm':
					translateX = atoi(argv[i+1]);
					break;
				case 'n':
					translateY = atoi(argv[i+1]);
					break;
				case 'r':
					rotation = DEG2RAD(atoi(argv[i+1]));
					break;
				case 'a':
					worldXMin = atoi(argv[i+1]);
					break;
				case 'b':
					worldYMin = atoi(argv[i+1]);
					break;
				case 'c':
					worldXMax = atoi(argv[i+1]);
					break;
				case 'd':
					worldYMax = atoi(argv[i+1]);
					break;

			}
		}
	}
}