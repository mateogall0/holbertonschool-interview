#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/*
 * insert_node - add a new node to sorted list
 * @head: head of linked list
 * @number: int
 * Return: listint_t pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t));
    listint_t *p = *head;
    listint_t *temp = NULL;

    if (!new)
        return NULL;
    new->n = number;
    new->next = NULL;

    if (!p)
    {
        *head = new;
        return new;
    }
    for (; p->next; p = p->next)
        if (p->n > number || p->next->n > number)
            break;

    if (p->n > number)
    {
        *head = new;
        new->next = p;
    }
    else
    {
        temp = p->next;
        p->next = new;
        new->next = temp;
    }
    return new;
}
