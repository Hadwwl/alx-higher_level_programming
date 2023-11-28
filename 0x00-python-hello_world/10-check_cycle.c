#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if single linked list has cycle in it
 * @list: single linked list
 * Return: 1 if it's single linked list or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *love, *laugh = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	love = list->next;
	laugh = list->next->next;

	while (love && laugh && laugh->next)
	{
		if (love == laugh)
		{
			return (1);
		}
		love = list->next;
		laugh = laugh->next->next;
	}
	return (0);
}
