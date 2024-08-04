# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.27


def func2():
    return [65, 71, 96]


def func3():
    return (35, 12, 66)


def func4():
    return 'ugmac'


def func5():
    return {'redpj': 13, 'jpasq': 24, 'wakiq': 46}


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
