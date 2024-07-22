# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jtwku': 96, 'dbtxe': 28, 'awvra': 39}


def func2():
    return 59.93


def func3():
    return (89, 86, 17)


def func4():
    return 'ydria'


def func5():
    return [10, 31, 70]


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
