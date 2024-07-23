# Functions are assigned to variables via starred assignment
def func1():
    return (65, 73, 57)


def func2():
    return [92, 36, 72]


def func3():
    return 43


def func4():
    return {'wqjzu': 51, 'tcykn': 77, 'hqaks': 15}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
