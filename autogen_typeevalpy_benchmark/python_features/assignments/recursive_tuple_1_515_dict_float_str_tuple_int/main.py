# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'txshm': 69, 'vbjbq': 4, 'gkjru': 77}


def func2():
    return 85.51


def func3():
    return 'mqpal'


def func4():
    return (30, 100, 49)


def func5():
    return 29


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
