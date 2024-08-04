# Functions are assigned to variables via starred assignment
def func1():
    return {'jrubq': 94, 'kxuny': 35, 'bxpra': 50}


def func2():
    return 31


def func3():
    return 'mdesk'


def func4():
    return 72.76

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
