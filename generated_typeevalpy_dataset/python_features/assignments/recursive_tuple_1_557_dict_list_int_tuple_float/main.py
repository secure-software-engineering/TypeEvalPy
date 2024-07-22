# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uoeha': 37, 'ayhiu': 10, 'ziyrl': 78}


def func2():
    return [21, 82, 51]


def func3():
    return 35


def func4():
    return (6, 57, 81)


def func5():
    return 96.68


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
