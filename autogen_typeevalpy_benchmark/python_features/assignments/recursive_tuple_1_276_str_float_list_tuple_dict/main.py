# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pzpdf'


def func2():
    return 69.33


def func3():
    return [68, 53, 68]


def func4():
    return (43, 78, 32)


def func5():
    return {'hfeau': 71, 'wchvw': 21, 'nshfi': 78}


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
