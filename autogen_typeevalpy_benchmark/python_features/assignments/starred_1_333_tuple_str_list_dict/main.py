# Functions are assigned to variables via starred assignment
def func1():
    return (71, 39, 100)


def func2():
    return 'recom'


def func3():
    return [19, 53, 45]


def func4():
    return {'buhsc': 53, 'hvnqb': 51, 'isntk': 92}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
