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
	int res = 0, counter = 0;
	listint_t *node = NULL;

	if (head == NULL || *head == NULL)
		return (res);

	for (node = *head; node; node = node->next)
		counter += node->n;

	if (counter % 2 == 0)
		res = 1;

	return (res);
}
