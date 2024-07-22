# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uruux': 92, 'sywxd': 48, 'teeaz': 54}


def func2():
    return (47, 97, 26)


def func3():
    return 'xucxb'


def func4():
    return [26, 41, 75]


def func5():
    return 77


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
