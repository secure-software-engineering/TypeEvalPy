# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 81


def func2():
    return (80, 80, 71)


def func3():
    return 'npjly'


def func4():
    return 83.34


def func5():
    return {'uxzsa': 40, 'uvpaw': 43, 'rgzzc': 27}


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
