# Functions are assigned to variables via starred assignment
def func1():
    return 87.81


def func2():
    return 26


def func3():
    return 'jpevp'


def func4():
    return {'ltnax': 37, 'nezlg': 27, 'jfsfk': 82}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
