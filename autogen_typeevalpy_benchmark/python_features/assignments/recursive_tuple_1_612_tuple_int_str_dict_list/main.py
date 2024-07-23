# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 79, 57)


def func2():
    return 7


def func3():
    return 'jldut'


def func4():
    return {'kvhwr': 26, 'gxbcv': 71, 'gmxqt': 41}


def func5():
    return [58, 19, 98]


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
