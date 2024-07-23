# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return [81, 14, 28]


def func3():
    return (32, 23, 88)


def func4():
    return {'bhmqk': 76, 'culao': 86, 'dmfyx': 93}


def func5():
    return 'pmhyo'


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
