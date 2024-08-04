# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (37, 2, 69)


def func2():
    return {'hiefz': 14, 'phacs': 91, 'olufx': 15}


def func3():
    return 93.67


def func4():
    return 45


def func5():
    return [86, 4, 100]


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
