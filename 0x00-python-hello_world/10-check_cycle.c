#include "lists.h"

/**
 * check_cycle - Check if a linked list have a cycle.
 *
 * @list: Pointer to a linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *node = NULL;

	if (!list)
		return (1);

	node = list->next;

	while (node && node != list)
		node = node->next;

	return (node == list);
}
