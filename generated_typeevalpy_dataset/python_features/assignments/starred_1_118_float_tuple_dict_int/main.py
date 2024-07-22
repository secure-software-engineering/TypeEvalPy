# Functions are assigned to variables via starred assignment
def func1():
    return 18.2


def func2():
    return (33, 84, 25)


def func3():
    return {'rcvem': 82, 'vixqi': 77, 'yxnzt': 57}


def func4():
    return 26

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
