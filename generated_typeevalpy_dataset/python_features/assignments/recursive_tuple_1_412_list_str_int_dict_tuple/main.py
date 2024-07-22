# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [27, 48, 1]


def func2():
    return 'xsvti'


def func3():
    return 59


def func4():
    return {'acgla': 59, 'moffh': 40, 'llebv': 16}


def func5():
    return (39, 57, 100)


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
