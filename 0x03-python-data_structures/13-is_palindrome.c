#include "lists.h"
#include <stdio.h>

listint_t *validate_palindrome(listint_t *head, listint_t *node)
{
	if (node->next)
		head = validate_palindrome(head, node->next);

	if (!head || head->n != node->n)
		return (NULL);

	if (head->next)
		head = head->next;

	return (head);
}

/**
 * is_palindrome - Validate if a linked list is palindrome
 *
 * @head: Double pointer to a linked list.
 *
 * Return: 1 if the linked list is palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	node = *head;

	if (validate_palindrome(*head, node) == NULL)
		return (0);

	return (1);
}
