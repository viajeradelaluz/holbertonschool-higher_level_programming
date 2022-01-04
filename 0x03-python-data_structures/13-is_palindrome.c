#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Points to the first element of the list.
 * Return: 1 if the list is palindrome, otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int new_array[4096];
	int size_list = 0, half_size = 0, i = 0;

	if (!head)
		return (1);

	current = *head;
	while (current)
	{
		new_array[size_list] = current->n;
		current = current->next;
		size_list++;
	}

	size_list--;
	half_size = size_list / 2;

	for (i = 0; i <= half_size; i++, size_list--)
	{
		if (new_array[i] != new_array[size_list])
			return (0);
	}

	return (1);
}
