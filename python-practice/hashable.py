a = [1,2]
b = (1,2)

c = set()

try:
    c.add(a)
except TypeError as e:
    print(e)

try:
    c.add(b)
except TypeError as e:
    print(e)

print(c)