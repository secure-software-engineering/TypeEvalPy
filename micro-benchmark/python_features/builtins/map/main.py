# A function is applied to elements of a list via map.
def func(x):
    pass


for i in map(func, [1, 2, 3]):
    pass


def func2(x):
    return func(x)


for i in map(func2, [1, 2, 3]):
    pass


def func3(x):
    def func():
        return x

    return func


res = map(func3, [1, 2, 3])

for r in res:
    r()
