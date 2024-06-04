#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 *@head: a pointer to the head of the list
 *Return: 1 if true and 0 if false
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *current = NULL;
	listint_t *new_next = NULL;
	listint_t *first_half = *head;
	listint_t *second_half = NULL;

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
