# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (88, 86, 31)


def func2():
    return 12


def func3():
    return 'rgirq'


def func4():
    return 69.54


def func5():
    return [15, 37, 46]


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
