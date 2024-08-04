# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [16, 22, 36]


def func2():
    return 90.08


def func3():
    return 23


def func4():
    return 'uijgy'


def func5():
    return {'kpfjv': 25, 'hqqdn': 70, 'ohkww': 74}


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
