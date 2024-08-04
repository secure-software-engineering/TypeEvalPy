# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mfyny'


def func2():
    return (15, 35, 93)


def func3():
    return 48


def func4():
    return {'nrhru': 79, 'taoxg': 74, 'hvtro': 68}


def func5():
    return 92.26


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
