#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define DEG2RAD(x) (x*M_PI/180)

int world_x1 = 0, world_x2 = 499, world_y1 = 0, world_y2 = 499;
int width, height ;
char* fileName;

float scaleFactor = 1.0f;
double rotation = 0.0;
int translateX = 0, translateY = 0; 

typedef struct Vertex Vertex;

struct Vertex{
	int x, y;
};

typedef struct PolyList PolyList;

struct PolyList{
	Vertex *v;
	PolyList * next;
};

PolyList * polygon;

void processArgs(int, char*[]);

void readPS();

void printArray(PolyList *);

void addVertex(PolyList**, Vertex*);

void clipping();
void clipper(char);
Vertex * intersection(Vertex*, Vertex*, char);
char inside(char, Vertex);

void draw(char *);
void swap(int *, int *);
void printPixels(char *);

void scalePolygon();
void rotatePolygon();
void translatePolygon();

int
main(int argc, char * argv[]){

	fileName = malloc(sizeof(char) * 64);
	strcpy(fileName, "hw2_a.ps");

	processArgs(argc, argv);

	width = world_x2 - world_x1 + 1;
	height = world_y2 - world_y1 + 1;

	char * pixels = malloc(sizeof(char[height * width]));

	readPS();

	scalePolygon();
	rotatePolygon();
	translatePolygon();

	clipping();

	draw(pixels);
	printPixels(pixels);
	
	printArray(polygon);
}

///////////////////////////////////
// Argument Processing
//////////////////////////////////

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
					world_x1 = atoi(argv[i+1]);
					break;
				case 'b':
					world_y1 = atoi(argv[i+1]);
					break;
				case 'c':
					world_x2 = atoi(argv[i+1]);
					break;
				case 'd':
					world_y2 = atoi(argv[i+1]);
					break;

			}
		}
	}
}

/////////////////////////////////////
//READING THE FILE
/////////////////////////////////////
void
readPS(){
	
	char *BUF = malloc(sizeof(char) * 124); //Read in input
	char *type = malloc(sizeof(char) * 32);

	FILE *f = fopen(fileName,"r");

	//Ignore all text until %%%BEGIN is reached
	while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%BEGIN\n",8));

	//Read till %%%END is reached
	while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%END\n",6)){
		if(strlen(BUF) > 7){
			// printf("%s\n",BUF);
			int x, y;
			sscanf(BUF, "%d %d %s", &x, &y, type);
			//fprintf(stderr, "point at %d %d %d %d\n", cursorX, cursorY, x, y);

			Vertex *v = (Vertex *)malloc(sizeof(Vertex));
			v->x = x;
			v->y = y;

			addVertex(&polygon, v);

			// cursorX = x;
			// cursorY = y;
		} 
	}

	free(BUF);
	free(type);
	
}

/////////////////////////////////////
// The Add Function for Linked List
/////////////////////////////////////

void
addVertex(PolyList ** linkedList, Vertex * v){
	//True if first time we called addVertex
	if(*linkedList == NULL){
		*linkedList = (PolyList *)malloc(sizeof(PolyList));
		(*linkedList)->v = v;
		return;
	}

	//Get to the last time we added a value;
	PolyList *current = *linkedList;
	while(current->next != NULL)
		current = current->next;

	//current->next == NULL so give it a location, then add a vertex to it
	current->next = (PolyList *)malloc(sizeof(PolyList));
	current->next->v = v;
}

////////////////////////////////////////
//DEBUGGING TOOL FOR THE LINKED LIST
///////////////////////////////////////

void
printArray(PolyList * linkedList){
	fprintf(stderr, "LINKEDLIST CHECKER [] \n");
	for(PolyList *PolyPointer = linkedList; PolyPointer != NULL; PolyPointer = PolyPointer->next){
		Vertex * tempVertex = PolyPointer->v;
		fprintf(stderr, "%d %d\n", tempVertex->x, tempVertex->y);
	}
}

///////////////////////////////////////
// THE CLIPPING SECTION
//////////////////////////////////////

#define TOP 0
#define BOTTOM 1
#define LEFT 2
#define RIGHT 3

void
clipping()
	{
		//Sutherland-Hodgman clipping

		clipper(TOP);

		clipper(RIGHT);

		clipper(BOTTOM);

		clipper(LEFT);
	}

PolyList * tempPolyList; 

void
clipper(char clip_boundary) {


	for (PolyList *polyPointer = polygon; polyPointer->next != NULL; polyPointer = polyPointer->next){
		Vertex * v1 = polyPointer->v;

		//We reached the end of the linked list, loop back to beginning, else use linked list next vertex
		Vertex * v2 = polyPointer->next->v;
		// int x1 = polyPointer->v.x;
		// int y1 = polyPointer->v.y;
		// int x2 = polyPointer->next->v.x;
		// int y2 = polyPointer->next->v.y;

		if(inside(clip_boundary, *v1)){	
			if(polyPointer == polygon)
			 	addVertex(&tempPolyList, v1);

			if(inside(clip_boundary, *v2)){
				addVertex(&tempPolyList, v2);

			}else{
				Vertex * v = intersection(v1, v2, clip_boundary);
				addVertex(&tempPolyList, v);
			}
		}else{
			if(inside(clip_boundary, *v2)){
				Vertex * v = intersection(v2, v1, clip_boundary);
				addVertex(&tempPolyList, v);

				addVertex(&tempPolyList, v2);
			}
		}
	}

	//printArray(tempPolyList);

	//TODO: Deallocate before polybefore moving it's reference
	polygon->v = tempPolyList->v;
	polygon->next = tempPolyList->next;

	tempPolyList = NULL;
}

char 
inside(char clip_boundary, Vertex v){

		if(clip_boundary == TOP && v.y < world_y2)
			return 1;

		else if(clip_boundary == LEFT && v.x > world_x1)
			return 1;

		else if(clip_boundary == BOTTOM && v.y > world_y1)
			return 1;

		else if(clip_boundary == RIGHT && v.x < world_x2)
			return 1;

		return 0;

}

Vertex *
intersection(Vertex * v1, Vertex * v2, char clip_boundary){
	int dx = v2->x - v1->x;
	int dy = v2->y - v1->y;

	float slope = dy/(float)dx;

	Vertex * v = (Vertex *)malloc(sizeof(Vertex));

	//Vertical line condition
	if(dx == 0 || dy == 0)
	{
		if(clip_boundary == TOP)
		{
			v->x = v1->x;
			v->y = world_y2;
		}
		else if(clip_boundary == LEFT)
		{
			v->x = world_x1;
			v->y = v1->y;
		}
		else if(clip_boundary == BOTTOM)
		{
			v->x = v1->x;
			v->y = world_y1;
		}
		else if(clip_boundary == RIGHT)
		{
			v->x = world_x2;
			v->y = v1->y;
		}
		return v;
	}

	if(clip_boundary == LEFT){
		v->x = world_x1;
		v->y = (int) (slope * (world_x1 - v1->x) + v1->y);
	}
	if(clip_boundary == RIGHT){
		v->x = world_x2;
		v->y = (int) (slope * (world_x2 - v1->x) + v1->y);
	}
	if(clip_boundary == TOP){
		v->x = (int) ((world_y2 - v1->y)/slope + v1->x);
		v->y = world_y2;
	}
	if(clip_boundary == BOTTOM){
		v->x = (int) ((world_y1 - v1->y)/slope + v2->x);
		v->y = world_y1;
	}

	return v;

}

//////////////////////////////////////
// THE DRAWING SECTION
//////////////////////////////////////

void
draw(char * pixels){

	//Make everything white
	for (int i=0; i<height; i++){
		for (int j=0; j<width; j++){
			*(pixels + i * width + j) = '0';
		}	
    }

    //Loop through my linked list, use DDA to draw out each line
	for (PolyList *polyPointer = polygon; polyPointer->next != NULL; polyPointer = polyPointer->next){
		int x1 = polyPointer->v->x - world_x1;
		int y1 = polyPointer->v->y - world_y1;
		int x2 = polyPointer->next->v->x - world_x1;
		int y2 = polyPointer->next->v->y - world_y1;
		
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

	for (int i=height-1; i>=0; i--){
		for (int j=0; j<width; j++)
			printf("%c ", *(pixels + i * width + j));
		printf("\n");
	}
}


////////////////////////////
// TRANSFORMATIONS
////////////////////////////

void
scalePolygon(){
	for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
		Vertex *v = polyPointer->v;
		v->x = (int) (v->x * scaleFactor);
		v->y = (int) (v->y * scaleFactor);
	}
}

void
rotatePolygon(){
	int temp_x, temp_y;
	for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
		Vertex *v = polyPointer->v;
		temp_x = (int) (v->x * cos(rotation) - (v->y * sin(rotation)));
		temp_y = (int) (v->x * sin(rotation) + (v->y * cos(rotation)));
		v->x = temp_x;
		v->y = temp_y;
	}
}

void
translatePolygon(){
	for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
		Vertex *v = polyPointer->v;
		v->x = v->x + translateX;
		v->y = v->y + translateY;
	}
}
