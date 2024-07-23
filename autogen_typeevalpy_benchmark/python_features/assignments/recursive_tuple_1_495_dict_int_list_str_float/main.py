# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ylchc': 80, 'tggob': 99, 'vbwpi': 71}


def func2():
    return 27


def func3():
    return [82, 78, 59]


def func4():
    return 'ygzuq'


def func5():
    return 28.8


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
