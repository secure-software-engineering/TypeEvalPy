# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'suypj': 64, 'pqgjp': 50, 'txcce': 96}


def func2():
    return 26.2


def func3():
    return 29


def func4():
    return 'oeawd'


def func5():
    return (15, 49, 23)


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
