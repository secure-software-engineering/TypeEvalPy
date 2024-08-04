# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 18, 47]


def func2():
    return 40.32


def func3():
    return {'uwoew': 95, 'gopyx': 93, 'nnojf': 91}


def func4():
    return (48, 86, 66)


def func5():
    return 46


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
