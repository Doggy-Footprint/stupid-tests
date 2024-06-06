// gcc c_dynamic_type.c -o c_dynamic_type
// ./c_dynamic_type
/**
 * output
 * as type_A, a->a is 1
 * as type_B, a->a is 67305985
 * as type_B, a2->a is 67305985
 * as type_A, b2->a is 1
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char a;
    char b;
    char c;
    char d;
} type_A;

typedef struct {
    int a;
} type_B;

int main() {

    printf("sizeof type_A: %ld, sizeof type_B: %ld\n", sizeof(type_A), sizeof(type_B));

    void *a = malloc(sizeof(type_A));
    void *b = malloc(sizeof(type_B));

    type_A *a2 = a;
    {
        a2->a = 1;
        a2->b = 2;
        a2->c = 3;
        a2->d = 4;
    }
    type_B *b2 = b;
    {
        b2->a = 1;
    }

    printf("as type_A, a->a is %d\n", ((type_A *)a)->a);
    printf("as type_B, a->a is %d\n", ((type_B *)a)->a);
    /**
     * sizeof type_A: 4, sizeof type_B: 4
     * as type_A, a->a is 1
     * as type_B, a->a is 67305985
    */

    printf("as type_B, a2->a is %d\n", ((type_B *)a2)->a);
    /**
     * as type_B, a2->a is 67305985
    */

    printf("as type_A, b2->a is %d\n", ((type_A *)b2)->a);
    /**
     * as type_A, b2->a is 1
    */
    return 0;
}