# Functions are assigned to variables via starred assignment
def func1():
    return [32, 26, 33]


def func2():
    return {'ququz': 40, 'vkrfc': 80, 'chckw': 48}


def func3():
    return 'ksyyi'


def func4():
    return 46

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
