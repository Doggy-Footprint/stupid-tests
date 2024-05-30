/**
 * gcc c_memory_map -o app
*/

#include <stdio.h>
#include <stdlib.h>

/*
* C memory consists of 5 parts
* BSS(block started by symbol)
* DataSegment(Initialized global symbols)
* Text(code)
* Heap
* Stack
*/

int BSS[10000];
int DS[10000] = { 0 };

void print(const char* type, void *addr)
{
    printf("type: %s, \t address: %p\n", type, addr);
}

void dummy_func()
{
    return;
}

int main()
{
    int *heap_var = malloc(10000 * sizeof(int));
    int stack_var[10000] = { 0 };
    void (*fptr)(const char *, void *) = &print;
    void (*fptr2)(dummy_func) = &dummy_func;

    print("BSS", BSS); //Block Starting Symbol
    print("DS", DS); //Data Segmnet
    print("HEAP", heap_var);
    print("STACK", stack_var);
    print("fptr", fptr);
    print("fptr2", fptr2);

    return 0;
}
