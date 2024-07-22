# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jjbot': 82, 'eshoz': 9, 'vsmpj': 10}


def func2():
    return 29.7


def func3():
    return 91


def func4():
    return [37, 22, 14]


def func5():
    return 'shdci'


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
