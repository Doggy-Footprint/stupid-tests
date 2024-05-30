/**
 * gcc -c c_type_example.c -o app -O0
*/

#include <stdio.h>

int operate_integer(int a, int b);
double operate_double(double a, double b);

int main() {

    int i;
    double d;

    i = operate_integer(3, 4);
    d = operate_double(3.0, 4.0);

    return 0;
}

int operate_integer(int a, int b) {
    int c;
    c = a * b;
    return a + b;
}

double operate_double(double a, double b) {
    double c;
    c = a * b;
    return a + b;
}
