# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pfucv': 3, 'inttm': 96, 'ttrfr': 96}


def func2():
    return 'doucg'


def func3():
    return 85.91


def func4():
    return 17


def func5():
    return (74, 61, 40)


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
