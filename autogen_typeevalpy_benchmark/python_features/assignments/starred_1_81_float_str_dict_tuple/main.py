# Functions are assigned to variables via starred assignment
def func1():
    return 16.16


def func2():
    return 'wzfqd'


def func3():
    return {'iyilh': 54, 'vseow': 23, 'qvxvv': 14}


def func4():
    return (91, 24, 91)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
