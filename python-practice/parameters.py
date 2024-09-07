def test(arg1: int, arg2: int = 3, arg3: int = 5, *args, kwarg1:str = "abc", **kwargs):
    print(f"""
arg1: {arg1}
arg2: {arg2}
arg3: {arg3}
args: {args}
kwarg1: {kwarg1}
kwargs: {kwargs}
""")


test(1,arg3 = 7, arg2 = 11)


def test2(pos1, pos2):
    print(f"""
pos1: {pos1}
pos2: {pos2}
""")

test2(*[1,2])

def test3(*, kw1, kw2):
    print(f"""
kw1: {kw1}
kw2: {kw2}
""")

test3(**{'kw1': 1, 'kw2': 2})

def test4(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

test4(ab = 3, bc = 5, cd = 7)