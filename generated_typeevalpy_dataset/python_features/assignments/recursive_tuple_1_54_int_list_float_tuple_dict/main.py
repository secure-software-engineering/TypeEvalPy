# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82


def func2():
    return [58, 24, 13]


def func3():
    return 76.62


def func4():
    return (32, 40, 22)


def func5():
    return {'pqyys': 29, 'cobtq': 100, 'zynvr': 73}


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
