# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (38, 60, 67)


def func2():
    return [19, 89, 19]


def func3():
    return {'dihxs': 99, 'dxyww': 34, 'fwzpj': 97}


def func4():
    return 16.09


def func5():
    return 24


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
