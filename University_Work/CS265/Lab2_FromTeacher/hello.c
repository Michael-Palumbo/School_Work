#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *name = getenv( "USER" ) ;

	printf( "Hello, %s\n", name ) ;

	return( 0 ) ;
}
