# Functions are assigned to variables via starred assignment
def func1():
    return {'zaatf': 94, 'kmfys': 54, 'fijww': 65}


def func2():
    return 57


def func3():
    return (87, 55, 92)


def func4():
    return 'hjnyw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
