# Knowledge
---
## opcode
각각의 **OPCODE**는 특정 Instruction set이 제공하는 기능에 매핑된다.
### MOV
## operand
**OPERAND**는 **OPCODE**의 연산 대상이다. **OPCODE**의 종류에 따라 필요한 **OPERAND**가 다르다.
### r/m
**r**: register
**m**: memory address
### imm
**imm**: r 혹은 m이 아닌 Instruction에 저장된 값이다. 즉, 바이너리에 하드코딩되어 있는 값이다.


# Goal
---

**목표**: 컴파일 된 바이너리에서 변수가 어떻게 저장되는지 확인하고, 그 변수를 사용(참조, 변경 등)할 때, 어떻게 읽는지 확인한다.

예를 들어, 4 byte 크기의 `int`와 8 byte 크기의 `long`을 어떻게 구분하여 사용할 수 있는지를 확인한다.

# Plan
---
**계획**: 다음과 같은 c 코드를 컴파일한 후, 디스어샘블리 코드를 확인한다.
```c
// gcc -O0 main.c -o main

int main() {
    /**
     * long (8), int (4), short (2), char (1)
     * and unsigned variable of each.
     */
    long a = 0;
    unsigned long b = 1;
    int c = 2;
    ...
    unsigned short f = 5;
    char g = 6;
    unsigned char h = 7;

    /**
     * similar set of variables assigned from above variables.
     */
    long a2 = a;
    unsigned long b2 = b;
    int c2 = c;
    ...
    unsigned char h2 = h;

    return 0;
}
```
# Result
---
**결과1**: 상수 값을 통해 정의한 변수들

## long
```c
long a = 0;
```
```
48 C7 45 E0 00 00 00 00
MOV qword ptr [RBP + long_const], 0x0
```
**48**: REX prefix. 굳이 자세히 조사하지는 않았으나, 64 bit register를 사용하는 것과 관련된 opcode prefix

**C7**: **OPCODE: MOV**
- operand1: r/m 16, 32, 64
- operand2: imm 16, 32

**45 E0**: RBP 레지스터로부터 offset이 E0인 memory address(local variable)

**00 00 00 00**: 상수 0

## int

```c
int c = 2;
```
```
C7 45 D0 02 00 00 00
MOV dword ptr [RBP + int_s], 0x2
```

**C7**: **OPCODE: MOV**

**45 D0**: RBP 레지스터로부터 offset이 D0인 memory address(local variable)

**02 00 00 00**: 상수 2

## short

```c
short e = 4;
```
```
66 C7 45 C8 04 00
```

**66**: 16 bit 레지스터를 사용하기 위한 opcode prefix

**C7**: **OPCODE: MOV**

**45 C8**: RBP 레지스터로부터 offset이 C8인 memory address(local variable)

**04 00**: 상수 4

## char

```c
char g = 6;
```
```
C6 45 C4 06
```

**C6**: **OPCODE: MOV**
- operand1: r/m 8
- operand2: imm 8

**45 C4**: RBP 레지스터로부터 offset이 C4인 memory address(local variable)

**06**: 상수 6

## Summary

### short, int, long
**OPCODE**로 C7 *MOV*를 사용하는 것은 같으나, prefix를 이용해 사용하는 register의 크기를 16, 32, 64로 변경한다.

### char
**OPCODE**로 C6 *MOV*를 사용한다.

다른 변수를 사용할 때는 다른 OPCODE를 사용하거나, prefix를 다르게하여 컴파일된다.

