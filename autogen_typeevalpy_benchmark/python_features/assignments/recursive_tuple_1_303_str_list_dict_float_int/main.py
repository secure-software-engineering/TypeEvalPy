# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'whneh'


def func2():
    return [75, 36, 5]


def func3():
    return {'zxnqy': 31, 'ftadj': 51, 'xflxr': 8}


def func4():
    return 83.93


def func5():
    return 16


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
