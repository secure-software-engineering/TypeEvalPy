# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (66, 57, 100)


def func2():
    return {'vwaqv': 65, 'kprzu': 93, 'cddme': 15}


def func3():
    return 13.05


def func4():
    return 85


def func5():
    return 'efoeo'


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
