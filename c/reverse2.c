/*
Reverse

Input: multiple strings

Out: reverse what is submitted
*/

#include <stdio.h>
void print_result(char arg[]); //forward declaration


void reverse(int argc, char *argv[]) {

	int i = 0;

	for(i = (argc-1); i > 0; i--) {
		print_result(argv[i]);
	}
}

void print_result(char arg[]){

	int i = 0;
	int count = 0;

	for(i = 0; arg[i] != '\0'; i++) {
		count = count + 1;
	}

	for(i = count; i >= 0; i--) {
		printf("%c", arg[i]);
	}

	printf(" ");
}

int main(int argc, char *argv[])
{
	reverse(argc, argv);
	printf("\n");
	return 0;
}