# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'khlem': 2, 'cwojo': 23, 'jibjm': 48}


def func2():
    return 45


def func3():
    return [15, 21, 68]


def func4():
    return 16.95


def func5():
    return 'kfhzw'


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
