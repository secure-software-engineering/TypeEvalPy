# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (99, 53, 38)


def func2():
    return 14


def func3():
    return {'pcdwq': 73, 'pyovu': 10, 'wnzus': 12}


def func4():
    return 'xgyux'


def func5():
    return [82, 32, 20]


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
