# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (43, 21, 33)


def func2():
    return 88.03


def func3():
    return {'milwq': 47, 'iadkq': 51, 'fcnxi': 28}


def func4():
    return 3


def func5():
    return 'qjlre'


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
