# Functions are assigned to variables via starred assignment
def func1():
    return (71, 25, 80)


def func2():
    return 87.65


def func3():
    return 22


def func4():
    return {'gitvm': 15, 'dwios': 28, 'roihi': 80}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
