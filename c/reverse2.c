/*
Reverse

Input: multiple array values

Out: reverse what is submitted
*/

#include <stdio.h>
#include <string.h>


void print_result(char arg[]){

	int word_len = strlen(arg);

	for(word_len; word_len >= 0; word_len--) {
		printf("%c", arg[word_len]);
	}

	printf(" ");
}

void reverse(int argc, char *argv[]) {

	int i = 0;

	for(i = (argc-1); i > 0; i--) {
		print_result(argv[i]);
	}
}

int main(int argc, char *argv[])
{
	reverse(argc, argv);
	printf("\n");
	return 0;
}