// gcc fptr_as_parameter.c -out fptr_as_parameter

#include <stdio.h>

void func(int a)
{
	printf("number is %d", a);
	return;
}

void exec(void (*callback)(int), int a)
{
	(*callback)(a);
	return;
}

int main()
{
	void (*fptr)(int) = &func;
	exec(fptr, 3);

	return 0;
}