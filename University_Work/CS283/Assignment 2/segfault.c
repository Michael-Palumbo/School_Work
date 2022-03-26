/*
   This assignment is to help you learn how to debug
   compiler warnings/errors and other common errors
   in your code. For each part labeled P(n), there is
   a warning/error/problem that goes with it. Write
   down what the issue was in the `Error:` section of
   each problem. Submit `segfault.c` along with your
   fixes and error comments.
 */

// P0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Error:
Forgot to include strlib.h
 */

void fib(int* A, int n);

int
main(int argc, char *argv[]) {
	int buf[10];
	unsigned int i;
	char *str;
	char *printThisOne;
	char *word;
	int *integers;
	int foo;
	int *bar;
	char *someText;

	// P1
	for (i = 0; i < 10; ++i) {
		buf[i] = i;
	}
	for (i = 0; i < 10; ++i) {
		printf("Index %d = %d\n", i, buf[i]);
	}
	/* Error:
	Went outside the allocated space, 0-9
	%s print out a series of characters until it reaches a \0
	 - Both %s are replaced with %d to replace numbers
	 */

	// P2
	str = malloc(sizeof(char) * 19);
	strcpy(str, "Something is wrong");
	printThisOne = str;
	printf("%s\n", printThisOne);
	/* Error:
	You need to include strlib.h to run strcpy
	You didn't dedicate enough space for str, we want a string of legnth, so allocate 19 
	I'm guessing you want printThisOne to be printed, so I changed str from the first 2 lines (I will also change it in P7
	 */

	// P3	
	char temp_word[] = "Part 3";
	word = temp_word;
	*(word + 4) = '-';
	printf("%s\n", word);
	/* Error:
	Saving a string to a pointer, saves said string in read only format, so we create a temp_word to get that string, and then have word point to the neawly created array.
	 * */
	

	// P4
	integers = (int *) malloc(11 * sizeof(int));
	*(integers + 10) = 10;
	printf("Part 4: %d\n", *(integers + 10));
	free(integers);
	/* Error:
	Dedicate the next 10 spots for integers.
	you cannot call free if you did not call malloc, since you cannot free something that hasn't been dedicated. We fixed this by calling malloc.
	 */

	// P5
	printf("Print this whole line\n");
	/* Error:
	\0 is used to denote that the string has ended, we add another escape character to escape the escape or, since I just read the email, just remove it in its entirety.
	 */

	// P6
	unsigned int x = 2147483647;
	printf("%d is positive\n", x); 
	x += 1000000000;
	printf("%u is positive\n", x); 
	/* Error:
	x is unsigned which means it can hold 2^32 (ints are 32 bits) %d denotes that we are using replacing a signed interger which means we lose roughly 2 billion numbers, we can switch both or atleast the second print statement with %u, u for unsigned 
	*/

	// P7
	printf("Cleaning up memory from previous parts\n");
	free(str);
	//free(buf);
	/* Error:
	buf is not created by allocated space. aka it cannot free space that was allocated by malloc in the first place. If this conclusion is wrong please email at mp3492@drexel.edu to inform me of this misunderstanding.
	 */

	// P8
	fib(&foo, 7);
	printf("fib(7) = %d\n", foo);
	/* Error:
	C automatically passes by value, we want to pass a pointer, aka a reference to that value
	 */

	// P9
	//bar = 0;
	bar = malloc(sizeof(int));
	*bar = 123;
	printf("bar = %d\n", *bar);
	/* Error:
	bar doesn't have a location, so we are giving it a location through buffer, this also ensures the space won't be accidentally used by something else.
	bar = 0 is removed, while 0 is the ONLY literal that can be assigned to a pointer, it's only used to denote the null pointer
	 */

	// P10
	someText = (char *)malloc(sizeof(char) * 10);
	strcpy(someText, "testing");
	printf("someText = %s\n", someText);
	free(someText);
	/* Error:
	Changed malloc to something more proper
	You are printing, after it is freed...? I moved free below the print statement
	 */

	exit(0);
}

// fib calculates the nth fibonacci number and puts it in A.
// There is nothing wrong with this function.
void fib(int *A, int n)
{
	int temp;
	if (n == 0 || n == 1)
		*A = 1;
	else {
		fib(A, n - 1);
		temp = *A;
		fib(A, n - 2);
		*A += temp;
	}
}
