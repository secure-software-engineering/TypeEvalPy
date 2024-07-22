# Functions are assigned to variables via starred assignment
def func1():
    return 63.73


def func2():
    return 'hcclf'


def func3():
    return {'smlsl': 46, 'bbstb': 5, 'vfmah': 58}


def func4():
    return (35, 54, 8)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
