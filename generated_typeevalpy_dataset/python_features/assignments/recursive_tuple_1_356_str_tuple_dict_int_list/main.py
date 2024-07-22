# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'aqvqo'


def func2():
    return (22, 67, 33)


def func3():
    return {'kltvj': 34, 'diiak': 7, 'znfev': 10}


def func4():
    return 43


def func5():
    return [27, 91, 28]


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
