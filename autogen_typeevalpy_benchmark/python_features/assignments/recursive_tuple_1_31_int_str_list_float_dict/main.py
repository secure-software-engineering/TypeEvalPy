# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 64


def func2():
    return 'faffq'


def func3():
    return [31, 62, 95]


def func4():
    return 77.07


def func5():
    return {'vujkv': 26, 'aajod': 26, 'lqxjz': 37}


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
