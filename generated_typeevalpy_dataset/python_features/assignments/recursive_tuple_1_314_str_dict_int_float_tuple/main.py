# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yivdr'


def func2():
    return {'tlapi': 45, 'vjcpd': 43, 'lwhyt': 37}


def func3():
    return 52


def func4():
    return 72.13


def func5():
    return (79, 6, 30)


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
