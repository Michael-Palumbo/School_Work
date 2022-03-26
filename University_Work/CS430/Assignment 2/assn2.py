#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define DEG2RAD(x) (x*M_PI/180)

import sys
from math import sin, cos, radians

world_x1 = 0
world_x2 = 499
world_y1 = 0
world_y2 = 499
width = 0
height = 0
fileName = ""

scaleFactor = 1.0
rotation = 0.0
translateX, translateY = 0, 0


class Vertex():
	def __init__(self,x,y):
		self.x = x
		self.y = y

polygon = [] #Contains a list of vertexs


def processArgs():
	global fileName, scaleFactor, translateX, translateY, rotation, world_y1,world_x1,world_y2, world_x2

	argv = sys.argv
	for i in range(1,len(argv),2):
	#for(int i = 1; i < argc; i+=2){
		if argv[i][0] == '-':
			letter = argv[i][1]
			if letter == "f":
				strcpy(fileName, argv[i+1]);
			elif letter == 's':
				scaleFactor = float(argv[i+1]);
			elif letter == 'm':
				translateX = int(argv[i+1]);
			elif letter == 'n':
				translateY = int(argv[i+1]);
			elif letter == 'r':
				rotation = radians(int(argv[i+1]));
			elif letter == 'a':
				world_x1 = int(argv[i+1]);
			elif letter == 'b':
				world_y1 = int(argv[i+1]);
			elif letter == 'c':
				world_x2 = int(argv[i+1]);
			elif letter == 'd':
				world_y2 = int(argv[i+1]);

			
#/////////////////////////////////////
#//READING THE FILE
#/////////////////////////////////////

def readPS():
	global polygon
	line = ""
	f = open(fileName,"r");
	#Ignore all text until %%%BEGIN is reached
	line = f.readline()
	# print(line,70, file=sys.stderr)
	while line != "%%%BEGIN\n":
		line = f.readline()

	#while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%BEGIN\n",8));

	#//Read till %%%END is reached
	line = f.readline()

	while line != "%%%END\n":
		if line != "stroke\n":
			x, y, word = line.split(" ")
			v = Vertex(int(x),int(y))
			polygon.append(v)

		line = f.readline()

	# while(strncmp(fgets(BUF, sizeof(char) * 124, f), "%%%END\n",6)){
	# 	if(strlen(BUF) > 7){
	# 		// printf("%s\n",BUF);
	# 		int x, y;
	# 		sscanf(BUF, "%d %d %s", &x, &y, type);
	# 		//fprintf(stderr, "point at %d %d %d %d\n", cursorX, cursorY, x, y);

	# 		Vertex *v = (Vertex *)malloc(sizeof(Vertex));
	# 		v->x = x;
	# 		v->y = y;

	# 		addVertex(&polygon, v);

	# 		// cursorX = x;
	# 		// cursorY = y;
	# 	} 
	# }

	f.close()

# /////////////////////////////////////
# // The Add Function for Linked List
# /////////////////////////////////////


# addVertex(v)

# 	//True if first time we called addVertex
# 	if(*linkedList == NULL){
# 		*linkedList = (PolyList *)malloc(sizeof(PolyList));
# 		(*linkedList)->v = v;
# 		return;
# 	}

# 	//Get to the last time we added a value;
# 	PolyList *current = *linkedList;
# 	while(current->next != NULL)
# 		current = current->next;

# 	//current->next == NULL so give it a location, then add a vertex to it
# 	current->next = (PolyList *)malloc(sizeof(PolyList));
# 	current->next->v = v;
# }

# ////////////////////////////////////////
# //DEBUGGING TOOL FOR THE LINKED LIST
# ///////////////////////////////////////


def printArray(array):
	print( "ARRAY CHECKER [] ", file=sys.stderr)
	for vertex in polygon:	
		print("%d %d"%( vertex.x, vertex.y), file=sys.stderr)

# ///////////////////////////////////////
# // THE CLIPPING SECTION
# //////////////////////////////////////

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3

def clipping():

		#Sutherland-Hodgman clipping

		clipper(TOP)

		clipper(RIGHT)

		clipper(BOTTOM)

		clipper(LEFT)

def clipper(clip_boundary):
	global polygon

	# for (PolyList *polyPointer = polygon; polyPointer->next != NULL; polyPointer = polyPointer->next){
	# 	Vertex * v1 = polyPointer->v;
	# 	//We reached the end of the linked list, loop back to beginning, else use linked list next vertex
	# 	Vertex * v2 = polyPointer->next->v;

	tempArray = []

	for i in range(len(polygon)-1):
		v1 = polygon[i]
		v2 = polygon[i+1]

		if inside(clip_boundary, v1):
			if i == 0:
				tempArray.append(v1)
			 	# addVertex(&tempPolyList, v1);

			if(inside(clip_boundary, v2)):
				tempArray.append(v2)
				# addVertex(&tempPolyList, v2);

			else:
				v = intersection(v1, v2, clip_boundary)
				tempArray.append(v)
				# addVertex(&tempPolyList, v);
			
		else:
			if inside(clip_boundary, v2):
				v = intersection(v2, v1, clip_boundary)
				tempArray.append(v)
				tempArray.append(v2)
				# addVertex(&tempPolyList, v)

				# addVertex(&tempPolyList, v2)

	polygon = tempArray
	# //printArray(tempPolyList);

	# //TODO: Deallocate before polybefore moving it's reference


	# polygon->v = tempPolyList->v;
	# polygon->next = tempPolyList->next;

	# tempPolyList = NULL;

def inside(clip_boundary, v):

		if (clip_boundary == TOP and v.y < world_y2):
			return True

		elif(clip_boundary == LEFT and v.x > world_x1):
			return True

		elif(clip_boundary == BOTTOM and v.y > world_y1):
			return True

		elif(clip_boundary == RIGHT and v.x < world_x2):
			return True

		return False


def intersection(v1, v2, clip_boundary):
	dx = v2.x - v1.x
	dy = v2.y - v1.y

	v = Vertex(0,0)

	# //Vertical line condition
	if(dx == 0 or dy == 0):
		if(clip_boundary == TOP):
			v.x = v1.x;
			v.y = world_y2;
		elif (clip_boundary == LEFT):
			v.x = world_x1
			v.y = v1.y
		elif (clip_boundary == BOTTOM):
			v.x = v1.x
			v.y = world_y1
		elif (clip_boundary == RIGHT):
			v.x = world_x2
			v.y = v1.y
		return v
	
	slope = dy/dx;

	if(clip_boundary == LEFT):
		v.x = world_x1
		v.y = (int) (slope * (world_x1 - v1.x) + v1.y)
	
	if(clip_boundary == RIGHT):
		v.x = world_x2
		v.y = (int) (slope * (world_x2 - v1.x) + v1.y)
	if(clip_boundary == TOP):
		v.x = (int) ((world_y2 - v1.y)/slope + v1.x)
		v.y = world_y2
	
	if(clip_boundary == BOTTOM):
		v.x = (int) ((world_y1 - v1.y)/slope + v2.x)
		v.y = world_y1

	return v

# //////////////////////////////////////
# // THE DRAWING SECTION
# //////////////////////////////////////

def draw(pixels):
	# //Make everything white
	for i in range(height):
		for j in range(width):
			pixels[i][j] = '0'
	# for (int i=0; i<height; i++){
	# 	for (int j=0; j<width; j++){
	# 		*(pixels + i * width + j) = '0';
	# 	}	
 #    }

    # //Loop through my linked list, use DDA to draw out each line
	# for (PolyList *polyPointer = polygon; polyPointer->next != NULL; polyPointer = polyPointer->next){
	
	for i in range(len(polygon) - 1 ):

		x1 = polygon[i].x - world_x1
		y1 = polygon[i].y - world_y1
		x2 = polygon[i+1].x - world_x1
		y2 = polygon[i+1].y - world_y1

		# print("Initial values", x1,y1,x2,y2, file=sys.stderr)


		# int x1 = polyPointer->v->x - world_x1;
		# int y1 = polyPointer->v->y - world_y1;
		# int x2 = polyPointer->next->v->x - world_x1;
		# int y2 = polyPointer->next->v->y - world_y1;
		
		steep = (abs(y2 - y1) > abs(x2 - x1));

		# print("steep", steep, file=sys.stderr)


		# //Slope greater than 1
		if(steep):
			(y1, x1) = (x1,y1)
			(y2, x2) = (x2,y2)

			# swap(&x1, &y1)
			# swap(&x2, &y2)

		# // Line heads left, swap points
		if(x1 > x2):
			(x1, x2) = (x2, x1)
			(y1, y2) = (y2, y1)
			# swap(&x1, &x2)
			# swap(&y1, &y2)

		# print("swapped values", x1,y1,x2,y2, file=sys.stderr)


		dErr = abs(y2 - y1)
		yStep = -1 if y1 > y2 else 1
		dX = x2 - x1

		err = dX / 2

		y = y1

		# print("extra", dErr, yStep, dX, err, y, file=sys.stderr)

		# for(int x = x1; x < x2; x++){
		for x in range(x1,x2):
			if steep:
				pixels[int(x)][int(y)] = '1' #drawPoint(y,x);
				# *((pixels+x*width)+y) = '1'; //drawPoint(y,x);
			else:

				pixels[int(y)][int(x)] = '1' #drawPoint(x,y);
				#*((pixels+y*width)+x) = '1'; //drawPoint(x,y);
			err -= dErr
			if(err < 0):
				y += yStep
				err += dX

def printPixels(pixels):
	print("P1");
	print("# test.pbm");
	print(width, height);

	for i in range(height-1, -1, -1):
		for j in range(width):
			print(pixels[i][j], end = " ")
		print()
# 	for (int i=height-1; i>=0; i--){
# 		for (int j=0; j<width; j++)
# 			printf("%c ", *(pixels + i * width + j));
# 		printf("\n");
# 	}
# }


# ////////////////////////////
# // TRANSFORMATIONS
# ////////////////////////////

def scalePolygon():

	for v in polygon:
		v.x = int( v.x * scaleFactor)
		v.y = int( v.y * scaleFactor)

# 	for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
# 		Vertex *v = polyPointer->v;
# 		v->x = (int) (v->x * scaleFactor);
# 		v->y = (int) (v->y * scaleFactor);
# 	}
# }

def rotatePolygon():
	# int temp_x, temp_y
	# for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
	# 	Vertex *v = polyPointer->v;
	for v in polygon:
		temp_x = int( (v.x * cos(rotation) - (v.y * sin(rotation))) )
		temp_y = int( (v.x * sin(rotation) + (v.y * cos(rotation))) )
		v.x = temp_x;
		v.y = temp_y;

def translatePolygon():
	# for (PolyList *polyPointer = polygon; polyPointer != NULL; polyPointer = polyPointer->next){
	# 	Vertex *v = polyPointer->v;
	for v in polygon:
		v.x += translateX;
		v.y += translateY;


if __name__ == "__main__":

	fileName = "hw2_a.ps"

	processArgs()

	width = world_x2 - world_x1 + 1
	height = world_y2 - world_y1 + 1

	#pixels = [["0"]*width]*height #malloc(sizeof(char[height * width]))

	pixels = []
	for i in range(height):
		col = []
		for i in range(width):
			col.append("0")
		pixels.append(col)

	readPS()

	scalePolygon()
	rotatePolygon()
	translatePolygon()

	clipping()

	draw(pixels)

	printPixels(pixels)
	
	printArray(polygon)

	#print("COMPLETE")