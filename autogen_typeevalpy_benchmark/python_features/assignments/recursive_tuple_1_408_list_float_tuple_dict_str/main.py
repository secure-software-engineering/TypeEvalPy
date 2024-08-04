# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [3, 100, 13]


def func2():
    return 23.66


def func3():
    return (59, 16, 19)


def func4():
    return {'hljij': 55, 'hyfay': 16, 'xuazy': 47}


def func5():
    return 'pmohe'


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
