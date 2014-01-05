/*
Reverse 

Input: single array value

Out: reverse of what is submitted

*/

#include <stdio.h>


int main(int argc, char *argv[])
{

	int i = 0;
	int j = 0;
	int count = 0;

	for(i = 0; argv[1][i] != '\0'; i++){
		count = count + 1;
	}

	for(j = count; j >= 0; j--) {
		char letter = argv[1][j];

    	printf("%c", letter);

		}

	printf("\n");
	return 0;
}