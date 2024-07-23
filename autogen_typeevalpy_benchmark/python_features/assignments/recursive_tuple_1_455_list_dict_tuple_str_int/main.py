# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [79, 53, 65]


def func2():
    return {'faysc': 68, 'oyiqp': 10, 'mftrg': 16}


def func3():
    return (63, 19, 18)


def func4():
    return 'ricnx'


def func5():
    return 80


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
