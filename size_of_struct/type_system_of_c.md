# Goal
---

C에서 variable을 사용할 때, 어떻게 메모리 상에서 읽어오는지 확인하기

# Practice
---

1. 동일한 크기의 struct 2개를 만들되, 하나는 char 4개, 하나는 int 1개를 포함하도록 작성한다.

```c
typedef struct {
    char a;
    char b;
    char c;
    char d;
} type_A;

typedef struct {
    int a;
} type_B;
```
```c
printf("sizeof type_A: %ld, sizeof type_B: %ld\n", sizeof(type_A), sizeof(type_B));
// sizeof type_A: 4, sizeof type_B: 4
```

2. 초기 값 설정
```c
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
```

3. 결과 확인

`type_A`를 `type_B`로 케스팅 했을 때, 몇 byte를 읽는지 확인
```c
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
```

4. 결론

C는 사용하는 데이터 타입에 따라 읽어들이는 바이트가 정해진다. 