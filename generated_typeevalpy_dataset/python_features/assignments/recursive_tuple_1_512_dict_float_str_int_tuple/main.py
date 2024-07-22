# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hlltm': 65, 'aispm': 35, 'zgmyb': 33}


def func2():
    return 53.03


def func3():
    return 'zsqql'


def func4():
    return 37


def func5():
    return (83, 33, 96)


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
