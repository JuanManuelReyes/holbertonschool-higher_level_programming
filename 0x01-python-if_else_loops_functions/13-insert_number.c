#include "lists.h"
/**
 *insert_node - asd
 *@head: asd
 *@number: asd
 *Return: asd
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *aux = *head, *prev = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	}
	else
	{
		while (number > aux->n && aux->next != NULL)
		{
			prev = aux;
			aux = aux->next;
		}
		if (number > aux->n)
		{
			aux->next = new_node;
			new_node->next = NULL;
		}
		else if (prev == NULL)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
			new_node->next = aux;
			prev->next = new_node;
		}
	}
	return (*head);
}
