# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ivfhf'


def func2():
    return 15


def func3():
    return {'tepxl': 62, 'hnxna': 97, 'fbutu': 63}


def func4():
    return [61, 39, 24]


def func5():
    return 33.87


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
