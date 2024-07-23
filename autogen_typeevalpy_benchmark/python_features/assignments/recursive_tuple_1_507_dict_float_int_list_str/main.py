# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hnvpy': 75, 'ysbxr': 91, 'tykce': 32}


def func2():
    return 92.34


def func3():
    return 36


def func4():
    return [16, 74, 91]


def func5():
    return 'twcnv'


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
