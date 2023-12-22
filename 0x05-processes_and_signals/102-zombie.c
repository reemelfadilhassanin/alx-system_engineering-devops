#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Function to create infinite while loop.
 *
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * new_process - function to create a new process
 * prints the PID of the new process.
 */
void new_process(void)
{
	int c = fork();

	if (c == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - entery point of prog.
 *
 * Return: alwys0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		new_process();
	}
	return (infinite_while());
}
