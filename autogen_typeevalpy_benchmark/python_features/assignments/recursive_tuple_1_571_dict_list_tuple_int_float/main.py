# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ypsfi': 10, 'vekil': 14, 'vrzov': 74}


def func2():
    return [59, 62, 21]


def func3():
    return (5, 7, 8)


def func4():
    return 14


def func5():
    return 41.22


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
