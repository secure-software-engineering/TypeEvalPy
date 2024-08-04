# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [23, 65, 17]


def func2():
    return 31.15


def func3():
    return 'pdcsz'


def func4():
    return {'ayabe': 42, 'hqpwb': 41, 'gqvzd': 9}


def func5():
    return 27


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
