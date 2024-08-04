# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ibazk'


def func2():
    return 46


def func3():
    return {'zbvwt': 27, 'nejsx': 64, 'cyxsb': 27}


def func4():
    return 57.54


def func5():
    return [79, 2, 6]


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
