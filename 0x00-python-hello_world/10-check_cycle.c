include "lists.h"

/**
 * check_cycle - Function to check if linked list has a cycle or not
 * @list: Pointer to head of linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	slow = fast = list;

	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
