# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'aueef'


def func2():
    return {'hzhdd': 29, 'dgegv': 98, 'petbl': 70}


def func3():
    return 65


def func4():
    return 77.72


def func5():
    return [62, 64, 53]


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
