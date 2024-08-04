# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vfjkt'


def func2():
    return [14, 29, 82]


def func3():
    return 83


def func4():
    return {'lvxea': 13, 'uncdb': 25, 'ygkvo': 4}


def func5():
    return (3, 4, 38)


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
