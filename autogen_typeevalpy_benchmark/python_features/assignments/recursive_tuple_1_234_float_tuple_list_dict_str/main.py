# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47.33


def func2():
    return (18, 93, 39)


def func3():
    return [1, 10, 33]


def func4():
    return {'srftp': 54, 'btdme': 51, 'zzzke': 76}


def func5():
    return 'fvbzh'


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
