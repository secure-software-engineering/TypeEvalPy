# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return (7, 28, 3)


def func3():
    return 'yrhqc'


def func4():
    return {'bkhsw': 54, 'nrgvc': 62, 'xitej': 61}


def func5():
    return 54.02


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
