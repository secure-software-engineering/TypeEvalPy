# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kksdo': 61, 'lbkic': 38, 'ibriz': 95}


def func2():
    return (99, 2, 58)


def func3():
    return 88


def func4():
    return [86, 13, 91]


def func5():
    return 'vepuo'


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
