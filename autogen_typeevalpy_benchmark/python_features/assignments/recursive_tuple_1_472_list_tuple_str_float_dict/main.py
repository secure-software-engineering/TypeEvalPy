# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [70, 51, 17]


def func2():
    return (5, 67, 90)


def func3():
    return 'kkegz'


def func4():
    return 78.2


def func5():
    return {'sdtlm': 53, 'wlish': 6, 'ktgnj': 17}


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
