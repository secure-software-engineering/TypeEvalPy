# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50


def func2():
    return [81, 1, 45]


def func3():
    return {'pguzj': 31, 'eqpwd': 61, 'dmxmk': 21}


def func4():
    return (57, 89, 77)


def func5():
    return 67.49


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
