# Functions are assigned to variables via starred assignment
def func1():
    return [56, 17, 19]


def func2():
    return (84, 76, 75)


def func3():
    return {'hnqum': 26, 'buxlw': 23, 'iamne': 7}


def func4():
    return 'usyqz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
