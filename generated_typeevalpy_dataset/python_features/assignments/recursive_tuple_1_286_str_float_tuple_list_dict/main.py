# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sbdqt'


def func2():
    return 23.9


def func3():
    return (74, 1, 41)


def func4():
    return [5, 72, 38]


def func5():
    return {'jiqke': 28, 'rmtqq': 33, 'vbkcm': 70}


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
