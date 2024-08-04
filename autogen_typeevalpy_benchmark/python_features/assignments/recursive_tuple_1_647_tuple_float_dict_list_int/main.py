# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (35, 3, 87)


def func2():
    return 65.15


def func3():
    return {'lujel': 46, 'doayv': 82, 'absen': 52}


def func4():
    return [34, 53, 94]


def func5():
    return 10


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
