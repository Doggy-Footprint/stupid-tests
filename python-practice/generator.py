def generator():
    yield (1,2,3)

a = generator()

print(type(a.__iter__))