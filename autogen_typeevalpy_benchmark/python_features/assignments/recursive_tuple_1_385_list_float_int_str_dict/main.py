# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [66, 63, 75]


def func2():
    return 14.78


def func3():
    return 64


def func4():
    return 'ybrir'


def func5():
    return {'ukowg': 21, 'iqnhg': 89, 'ollxg': 90}


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
