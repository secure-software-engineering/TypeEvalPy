# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (24, 59, 19)


def func2():
    return {'isvsh': 2, 'dcckq': 7, 'bowai': 1}


def func3():
    return 1


def func4():
    return 'egjdd'


def func5():
    return [81, 85, 43]


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
