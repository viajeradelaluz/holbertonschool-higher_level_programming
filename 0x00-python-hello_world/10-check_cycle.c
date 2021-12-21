#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it.
 * @list: points to the list.
 * Return: 1 if there is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	if (!list || !list->next)
		return (0);

	while (list && list->next)
	{
		if (list->next >= list || !list->next)
			break;

		list = list->next;
	}
	if (list->next)
		return (1);

	return (0);
}
