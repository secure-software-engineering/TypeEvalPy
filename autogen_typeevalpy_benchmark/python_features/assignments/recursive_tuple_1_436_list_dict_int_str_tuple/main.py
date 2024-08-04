# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [63, 88, 80]


def func2():
    return {'tzlxk': 10, 'frqre': 61, 'eevor': 46}


def func3():
    return 92


def func4():
    return 'aoubu'


def func5():
    return (32, 6, 33)


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
