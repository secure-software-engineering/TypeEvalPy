# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 58.89


def func2():
    return 'dghic'


def func3():
    return {'kzoqu': 56, 'xwadg': 4, 'oytda': 89}


def func4():
    return (22, 10, 17)


def func5():
    return 66


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
