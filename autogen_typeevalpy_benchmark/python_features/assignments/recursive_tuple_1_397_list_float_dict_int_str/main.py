# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [95, 33, 53]


def func2():
    return 93.81


def func3():
    return {'euuyy': 12, 'clfdc': 82, 'eyrak': 72}


def func4():
    return 57


def func5():
    return 'mabhq'


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
