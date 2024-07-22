# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [25, 81, 32]


def func2():
    return 75


def func3():
    return (80, 56, 95)


def func4():
    return {'rtdri': 4, 'wmgau': 39, 'iqmul': 12}


def func5():
    return 90.53


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
