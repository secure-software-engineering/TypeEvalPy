# Functions are assigned to variables via starred assignment
def func1():
    return (96, 58, 2)


def func2():
    return [35, 26, 25]


def func3():
    return {'gtrqn': 35, 'vfhkt': 60, 'cjmox': 29}


def func4():
    return 57

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
