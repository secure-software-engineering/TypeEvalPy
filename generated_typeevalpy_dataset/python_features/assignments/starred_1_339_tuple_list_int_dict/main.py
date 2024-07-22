# Functions are assigned to variables via starred assignment
def func1():
    return (89, 28, 5)


def func2():
    return [4, 13, 29]


def func3():
    return 59


def func4():
    return {'hylfo': 12, 'czvfb': 34, 'pkptq': 90}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
