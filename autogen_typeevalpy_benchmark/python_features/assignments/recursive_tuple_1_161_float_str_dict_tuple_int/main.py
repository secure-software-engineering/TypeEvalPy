# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7.11


def func2():
    return 'sqnuy'


def func3():
    return {'ermto': 33, 'xyevl': 38, 'buavy': 40}


def func4():
    return (63, 94, 63)


def func5():
    return 89


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
