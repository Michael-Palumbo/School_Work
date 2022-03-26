#include <stdio.h>
#include <stdlib.h>

void menu(int *choice){

	printf("Enter Game Menu\n--------------\n1) Rock\n2) Paper\n3) Scissors \n4) Quit\n\nEnter your choice: ");
	*choice = getchar() - '0';
	getchar(); //Washing out the enter key
}

int aiChoice(){
	return 1+ rand()%3;
}

int main(){
	int userchoice;
	while (1){
		menu(&userchoice);
		if (userchoice == 4)
			return 0;
		int aiC = aiChoice();

		if(userchoice == aiC)
			printf("Tie..?");
		else if(userchoice == 1){
			if(aiC == 3)
				printf("Congz fam you win");
			else
				printf("OOF You lost");
		}else if (userchoice == 2){
			if(aiC == 1)
				printf("Congz fam you win");
			else
				printf("OOF You Lost");
		}else if (userchoice == 3){
			if (aiC == 1)
				printf("OOf You lost");
			else
				printf("Congz fam you win");
		}

		printf("\nJust for reference, ai chose: %d\n\n",aiC);


		//printf("%d",userchoice);
	}
	return 0;
}
