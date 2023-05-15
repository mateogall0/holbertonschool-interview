#include "palindrome.h"


int is_palindrome(unsigned long n)
{
	int temp = n;
	int reversed = 0;
	int current;

	while(n != 0)
	{
		current = n % 10;
		reversed = reversed * 10 + current; 
		n /= 10;
	}

		return temp == reversed;
}