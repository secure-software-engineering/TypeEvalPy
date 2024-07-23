# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 93


def func2():
    return [8, 57, 14]


def func3():
    return 83.82


def func4():
    return (16, 86, 61)


def func5():
    return {'rajko': 14, 'xcbyx': 49, 'fefuh': 6}


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
