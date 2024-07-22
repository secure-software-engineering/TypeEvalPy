# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [53, 81, 35]


def func2():
    return {'ppkhv': 34, 'vrqhv': 42, 'sjpnb': 25}


def func3():
    return 'teyuh'


def func4():
    return (77, 59, 98)


def func5():
    return 97.72


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
