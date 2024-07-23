# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'plnob': 26, 'ufbdc': 68, 'yjqzj': 1}


def func2():
    return (61, 80, 61)


def func3():
    return 79.91


def func4():
    return 46


def func5():
    return 'gepcf'


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
