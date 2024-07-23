# Functions are assigned to variables via starred assignment
def func1():
    return {'jbagp': 72, 'gafbx': 30, 'rcoxj': 92}


def func2():
    return 'qpbwx'


def func3():
    return (10, 81, 87)


def func4():
    return [54, 32, 9]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
