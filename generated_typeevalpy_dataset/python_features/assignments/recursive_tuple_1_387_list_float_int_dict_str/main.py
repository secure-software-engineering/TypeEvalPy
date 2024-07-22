# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [57, 37, 7]


def func2():
    return 75.98


def func3():
    return 94


def func4():
    return {'nqsfz': 65, 'omagj': 63, 'grgqk': 25}


def func5():
    return 'dfxqs'


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
