#include "lists.h"


int check_cycle(listint_t *list)
{
	listint_t *p = NULL;

	if (!list || !list->next)
		return (0);

	for (p = list->next; p && p->next; p = p->next)
		if (p == list)
			return (1);

	return (0);
}
