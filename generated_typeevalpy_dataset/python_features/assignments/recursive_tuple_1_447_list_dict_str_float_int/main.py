# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [14, 85, 90]


def func2():
    return {'wjrhq': 22, 'lokqn': 24, 'ixxub': 11}


def func3():
    return 'pqelr'


def func4():
    return 95.07


def func5():
    return 9


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
