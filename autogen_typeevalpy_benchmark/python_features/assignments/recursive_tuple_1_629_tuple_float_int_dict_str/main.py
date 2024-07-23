# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (59, 95, 40)


def func2():
    return 1.41


def func3():
    return 60


def func4():
    return {'tbral': 60, 'cootp': 90, 'yomed': 33}


def func5():
    return 'fqeyz'


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
