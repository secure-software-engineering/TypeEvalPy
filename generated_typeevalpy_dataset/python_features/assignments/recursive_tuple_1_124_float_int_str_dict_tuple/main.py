# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35.67


def func2():
    return 4


def func3():
    return 'xjdal'


def func4():
    return {'jcord': 86, 'cbihv': 63, 'slrfy': 66}


def func5():
    return (79, 69, 60)


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
