# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28.89


def func2():
    return {'dmjxr': 77, 'gihvo': 15, 'ejaiq': 46}


def func3():
    return 94


def func4():
    return (5, 69, 95)


def func5():
    return 'kendd'


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
