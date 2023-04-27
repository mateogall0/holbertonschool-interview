#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if false, 1 if true
 */


int is_palindrome(listint_t **head)
{
	int arr[ARR_SIZE];
	int i = 0, j;
	listint_t *p = NULL;

	if (!head || !(*head))
		return 1;
	for (p = (*head); p; p = p->next, i++)
	{
		arr[i] = p->n;
	}
	for (j = 0; j <= i / 2; j++, i--)
	{
		if (arr[j] != arr[i])
			return 0;
	}
	return 1;
}