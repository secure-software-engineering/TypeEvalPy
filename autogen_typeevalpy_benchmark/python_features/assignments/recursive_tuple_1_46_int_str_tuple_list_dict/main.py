# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50


def func2():
    return 'unovi'


def func3():
    return (83, 72, 52)


def func4():
    return [30, 40, 77]


def func5():
    return {'efgkg': 23, 'qjhzp': 3, 'gmzoq': 68}


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
