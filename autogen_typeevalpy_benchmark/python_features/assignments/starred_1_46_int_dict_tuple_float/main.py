# Functions are assigned to variables via starred assignment
def func1():
    return 81


def func2():
    return {'zaoak': 72, 'izcad': 13, 'sazae': 40}


def func3():
    return (27, 44, 30)


def func4():
    return 88.59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
