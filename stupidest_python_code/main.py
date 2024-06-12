def foo() -> str:
    return ['a', 'b']

print(foo())

class A:
    def fooA(self) -> int:
        return [1, 'a']

a = A()

method = getattr(a, 'foo' + 'A')

print(method())
