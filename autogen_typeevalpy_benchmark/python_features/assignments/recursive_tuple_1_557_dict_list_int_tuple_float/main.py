# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bdwsv': 20, 'socnx': 51, 'qnptz': 19}


def func2():
    return [5, 68, 45]


def func3():
    return 65


def func4():
    return (9, 64, 34)


def func5():
    return 69.19


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
