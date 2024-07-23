# Functions are assigned to variables via starred assignment
def func1():
    return 72.86


def func2():
    return {'livmb': 92, 'iodvk': 3, 'yitcg': 21}


def func3():
    return (24, 100, 97)


def func4():
    return [34, 25, 16]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
