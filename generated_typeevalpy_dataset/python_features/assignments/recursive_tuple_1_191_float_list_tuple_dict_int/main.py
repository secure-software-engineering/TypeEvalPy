# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 85.83


def func2():
    return [34, 55, 20]


def func3():
    return (30, 58, 7)


def func4():
    return {'tdqxk': 54, 'zacjc': 22, 'tuqux': 6}


def func5():
    return 73


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
