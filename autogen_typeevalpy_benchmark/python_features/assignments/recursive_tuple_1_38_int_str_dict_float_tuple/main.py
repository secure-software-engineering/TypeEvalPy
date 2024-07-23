# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87


def func2():
    return 'pafeu'


def func3():
    return {'eunnf': 48, 'gyrhj': 58, 'elnqi': 94}


def func4():
    return 96.39


def func5():
    return (46, 11, 2)


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
