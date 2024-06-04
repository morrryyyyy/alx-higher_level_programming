#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 *@head: a pointer to the head of the list
 *Return: 1 if true and 0 if false
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *current;
	listint_t *new_next;
	listint_t *first_half;
	listint_t *second_half;

	slow = fast = *head;
	prev = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	current = slow;
	while (current != NULL)
	{
		new_next = current->next;
		current->next = prev;
		prev = current;
		current = new_next;
	}
	second_half = prev;
	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
