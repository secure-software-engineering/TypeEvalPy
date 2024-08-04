# Functions are assigned to variables via starred assignment
def func1():
    return 'jmrrb'


def func2():
    return {'kymbo': 39, 'vkbhn': 84, 'vffve': 43}


def func3():
    return 79.79


def func4():
    return (33, 79, 55)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
