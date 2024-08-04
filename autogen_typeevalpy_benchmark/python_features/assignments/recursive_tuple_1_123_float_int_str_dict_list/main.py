# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 11.17


def func2():
    return 29


def func3():
    return 'bacir'


def func4():
    return {'leexj': 79, 'xzywg': 49, 'ucybi': 35}


def func5():
    return [90, 22, 18]


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
