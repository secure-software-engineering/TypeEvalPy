# Functions are assigned to variables via starred assignment
def func1():
    return {'xsmhx': 75, 'pswki': 17, 'ocndi': 61}


def func2():
    return 'ptwch'


def func3():
    return 7.44


def func4():
    return [9, 29, 92]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
