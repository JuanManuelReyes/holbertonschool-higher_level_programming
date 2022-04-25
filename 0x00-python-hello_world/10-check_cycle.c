#include <stdio.h>
#include "lists.h"

/**
 * check_cycl - asd
 * Return: asd
 */
int check_cycle(listint_t *list)
{
	listint_t *two = list;
	listint_t *one = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		if (two->next != NULL && two->next->next != NULL)
		{
			two = two->next->next;
			one = one->next;

			if (two == one)
				return (1);
		}
		else
			return (0);
	}
}
