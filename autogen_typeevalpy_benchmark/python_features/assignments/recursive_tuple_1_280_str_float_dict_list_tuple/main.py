# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'edydw'


def func2():
    return 55.7


def func3():
    return {'jisoq': 92, 'qkiva': 92, 'hoowb': 17}


def func4():
    return [64, 9, 9]


def func5():
    return (18, 20, 14)


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
