# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 39, 3)


def func2():
    return 'bfdif'


def func3():
    return {'mrwjy': 27, 'jsexr': 91, 'rgnzu': 5}


def func4():
    return [18, 73, 12]


def func5():
    return 43


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
