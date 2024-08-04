# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [77, 16, 19]


def func2():
    return {'nyngo': 41, 'kqpzn': 62, 'uxtph': 75}


def func3():
    return 70.6


def func4():
    return 62


def func5():
    return 'cvrgg'


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
