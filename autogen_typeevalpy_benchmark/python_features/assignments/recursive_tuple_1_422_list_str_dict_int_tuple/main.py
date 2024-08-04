# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [7, 35, 6]


def func2():
    return 'pfdxc'


def func3():
    return {'pclmo': 85, 'gmrvo': 86, 'fsjul': 83}


def func4():
    return 51


def func5():
    return (24, 38, 82)


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
