# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gxwlq'


def func2():
    return {'oftfz': 81, 'twwpg': 43, 'weqlt': 72}


def func3():
    return 11.44


def func4():
    return [74, 90, 61]


def func5():
    return (52, 39, 54)


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
