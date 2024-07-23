# Functions are assigned to variables via starred assignment
def func1():
    return {'ftmos': 8, 'kajku': 12, 'aejrc': 3}


def func2():
    return [4, 58, 3]


def func3():
    return 27.03


def func4():
    return (76, 100, 23)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
