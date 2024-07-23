# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pagty': 59, 'qcliu': 65, 'antju': 68}


def func2():
    return (11, 99, 94)


def func3():
    return 28.52


def func4():
    return [27, 48, 71]


def func5():
    return 40


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
