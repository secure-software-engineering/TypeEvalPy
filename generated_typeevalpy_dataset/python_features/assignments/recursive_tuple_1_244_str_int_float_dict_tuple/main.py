# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'oryju'


def func2():
    return 4


def func3():
    return 23.36


def func4():
    return {'xoglz': 41, 'buixh': 26, 'pyhdn': 71}


def func5():
    return (89, 97, 52)


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
