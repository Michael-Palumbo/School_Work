#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Line is a linked list
struct Line{
	int x1, x2, y1, y2;
	struct Line * next;
};




int main(){
	struct Line *lhead = (struct Line *) malloc(sizeof(struct Line));
	loadPS(lhead);

	draw(lhead);
	return 0;
}

void drawLine(struct Line l){
	int dx, dy, D, x, y;
	dx = l.x2 - l.x1;
	dy = l.y2 - l.y1;
	D = 2*dy-dx;
	y = y1;
	for(x = l.x1; x <= l.x2; x++){
		drawPixel(x,y);
		if(D <= 0)
			D += 2*dy;
		else{
			D += 2*(dy-dx);
			y++
		}
	}
}


void drawReflexLine()


void loadPS(struct Line *head){
	char *BUF = malloc(sizeof(char) * 124);
	char *line = malloc(sizeof(char) * 124);
	char *type = malloc(sizeof(char) * 32); //Not really used yet
	struct Line *lcur = lhead;
	
	FILE *f = fopen("test.ps","r");

	printf("Start\n");

	do{
		fgets(BUF, sizeof(char) * 124, f);
		//printf("%s\n",BUF);
	}while(strncmp(BUF, "%%%BEGIN",8) != 0);

	printf("End Reading till start\n");

	fgets(BUF, sizeof(char) * 124, f);
	while(strncmp(BUF, "%%%END",6) != 0){
		strcpy(line,BUF);
		if(strlen(line) > 4){ 
			sscanf(BUF, "%d %d %d %d %s", &lcur->x1, &lcur->y1, &lcur->x2, &lcur->y2, type);
			lcur->next = (struct Line *)malloc(sizeof(struct Line));
			lcur = lcur->next;
		}
		fgets(BUF, sizeof(char) * 124, f);
	}

	printf("End of Reading\n");

	struct Line *lstart;

	for(lstart = lhead; lstart != NULL; lstart = lstart->next){
		printf("%d %d %d %d\n", lstart->x1, lstart->x2, lstart->y1, lstart->y2);
	}

	free(BUF);
	free(line);
	free(type);

}