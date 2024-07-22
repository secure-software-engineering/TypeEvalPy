# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 69


def func2():
    return 25.89


def func3():
    return {'mapeb': 88, 'xfvbd': 11, 'btwhm': 74}


def func4():
    return 'klgrg'


def func5():
    return (2, 50, 95)


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
