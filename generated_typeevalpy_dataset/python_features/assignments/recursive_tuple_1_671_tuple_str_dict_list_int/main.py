# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (6, 74, 64)


def func2():
    return 'ssupt'


def func3():
    return {'ybsac': 25, 'jtynr': 28, 'igrez': 91}


def func4():
    return [62, 16, 47]


def func5():
    return 32


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
