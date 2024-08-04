# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.8


def func2():
    return [38, 13, 29]


def func3():
    return 15


def func4():
    return 'zxtkl'


def func5():
    return {'gleyr': 28, 'jkdwv': 53, 'wprag': 8}


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
