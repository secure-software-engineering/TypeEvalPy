# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (8, 13, 13)


def func2():
    return [94, 29, 68]


def func3():
    return {'jcnta': 46, 'lkaaz': 23, 'njauy': 37}


def func4():
    return 'loylj'


def func5():
    return 43.57


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
