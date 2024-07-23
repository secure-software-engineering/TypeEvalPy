# Functions are assigned to variables via starred assignment
def func1():
    return 99.78


def func2():
    return {'cyyyc': 57, 'drbyd': 60, 'oyowk': 15}


def func3():
    return 53


def func4():
    return (17, 60, 76)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
