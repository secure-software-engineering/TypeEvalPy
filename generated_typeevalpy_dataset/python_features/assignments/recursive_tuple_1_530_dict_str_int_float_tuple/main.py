# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hsymn': 23, 'bivlq': 66, 'qfwsh': 31}


def func2():
    return 'oaqft'


def func3():
    return 56


def func4():
    return 61.0


def func5():
    return (20, 84, 90)


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
