# Functions are assigned to variables via starred assignment
def func1():
    return {'ntlhq': 44, 'ktauc': 83, 'djgus': 47}


def func2():
    return [74, 70, 80]


def func3():
    return (48, 5, 42)


def func4():
    return 'cquwi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
