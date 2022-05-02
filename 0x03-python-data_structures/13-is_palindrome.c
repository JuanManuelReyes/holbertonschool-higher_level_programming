#include "lists.h"

#include "lists.h"

/**
 * is_palindrome - asd
 * @head: asd
 * Return: asd
 */
int is_palindrome(listint_t **head)
{
        listint_t *aux = *head;
        int size = 0, i = 0, data[1024];

        /*No existe LL*/
        if (head == NULL)
                return (0);

        /*Ta vacia, es palindrome*/
        if (*head == NULL)
                return (1);

        /*Calcula el size*/
        while (aux != NULL)
        {
                aux = aux->next;
                size += 1;
        }
        /*Tiene un elemento, es palindrome*/
        if (size == 1)
                return (1);

        aux = *head;
        /*Compara con data*/
        while (aux != NULL)
        {
                data[i++] = aux->n;
                aux = aux->next;
        }

        for (i = 0; i <= (size / 2); i++)
        {
                if (data[i] != data[size - i - 1])
                        return (0);
        }
        return (1);
}

