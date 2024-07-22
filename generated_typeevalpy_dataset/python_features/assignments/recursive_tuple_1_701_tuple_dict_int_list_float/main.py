# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (35, 94, 81)


def func2():
    return {'chnca': 60, 'rarpk': 92, 'bfban': 80}


def func3():
    return 4


def func4():
    return [68, 73, 16]


def func5():
    return 16.54


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
