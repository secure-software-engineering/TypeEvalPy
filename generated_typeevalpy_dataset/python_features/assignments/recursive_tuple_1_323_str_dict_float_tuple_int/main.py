# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yxsuj'


def func2():
    return {'dcadz': 59, 'alimt': 19, 'aggha': 20}


def func3():
    return 26.26


def func4():
    return (73, 66, 69)


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
