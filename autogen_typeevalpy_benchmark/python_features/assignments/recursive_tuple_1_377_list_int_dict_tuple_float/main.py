# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [69, 14, 19]


def func2():
    return 60


def func3():
    return {'tmnxb': 22, 'vqwxp': 74, 'vcfnz': 70}


def func4():
    return (44, 95, 63)


def func5():
    return 78.66


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
