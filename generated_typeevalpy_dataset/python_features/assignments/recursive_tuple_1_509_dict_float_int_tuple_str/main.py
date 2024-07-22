# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qxfce': 15, 'mkfja': 7, 'uuvzu': 79}


def func2():
    return 62.11


def func3():
    return 29


def func4():
    return (83, 24, 74)


def func5():
    return 'ngkpr'


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
