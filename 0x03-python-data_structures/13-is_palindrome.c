#include "lists.h"

/**
 * is_palindrome - Validate if a linked list is palindrome
 *
 * @head: Double pointer to a linked list.
 *
 * Return: 1 if the linked list is palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int res = 1, size = 0, i = 0, j = 0;
	listint_t *node = NULL;
	char *new_string = NULL;

	if (head == NULL || *head == NULL)
		return (res);

	for (node = *head; node; node = node->next)
		size++;

	new_string = malloc(sizeof(char) * size);
	if (!new_string)
		return (0);

	for (node = *head; node; node = node->next, i++)
		new_string[i] = node->n;

	for (i = 0, j = size - 1; new_string[i]; i++, j--)
	{
		if (i > j)
			break;
		if (new_string[i] != new_string[j])
			return (0);
	}

	free(new_string);

	return (res);
}
