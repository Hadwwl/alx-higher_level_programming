#include "lists.h"

/**
 * is_palindrome - checks palind numbers
 * @head: the head of list
 * Return: 0 if no palindome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (d_palindrome(head, *head));
}
/**
 * d_palindrome - assist
 * @head: the head of list
 * @tail: the end of the list
 * Return: 1
 */
int d_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
	{
		return (1);
	}
	if (d_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
