#include <string.h>



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