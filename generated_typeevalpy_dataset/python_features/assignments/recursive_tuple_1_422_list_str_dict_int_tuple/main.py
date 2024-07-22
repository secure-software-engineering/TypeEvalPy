# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [73, 48, 17]


def func2():
    return 'lujmx'


def func3():
    return {'eecjg': 17, 'bwrgt': 19, 'jigxf': 69}


def func4():
    return 43


def func5():
    return (46, 61, 38)


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
