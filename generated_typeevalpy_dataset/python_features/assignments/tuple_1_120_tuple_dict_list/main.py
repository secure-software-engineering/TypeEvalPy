# Two variables are assigned a value via a tuple assignment.
def func1():
    return (17, 58, 60)


def func2():
    return {'azjwe': 83, 'nhxvn': 13, 'gssji': 36}


def func3():
    return [11, 43, 84]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
