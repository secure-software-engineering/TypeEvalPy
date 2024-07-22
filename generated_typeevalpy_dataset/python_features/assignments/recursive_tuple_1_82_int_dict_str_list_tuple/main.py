# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 45


def func2():
    return {'phxqu': 46, 'bdybo': 13, 'zskze': 28}


def func3():
    return 'nueug'


def func4():
    return [30, 100, 61]


def func5():
    return (63, 47, 61)


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
