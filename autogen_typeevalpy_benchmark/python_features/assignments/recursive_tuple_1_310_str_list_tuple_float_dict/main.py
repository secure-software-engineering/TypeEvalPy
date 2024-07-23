# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ycgwf'


def func2():
    return [94, 90, 94]


def func3():
    return (11, 24, 84)


def func4():
    return 21.76


def func5():
    return {'eeyay': 63, 'coqif': 32, 'iuksa': 42}


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
