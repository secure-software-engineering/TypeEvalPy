# Functions are assigned to variables via starred assignment
def func1():
    return [83, 97, 9]


def func2():
    return (44, 82, 87)


def func3():
    return {'gdobo': 10, 'htpbe': 47, 'kuisz': 16}


def func4():
    return 22.57

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
