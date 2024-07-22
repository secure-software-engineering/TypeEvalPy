# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mkhfw': 83, 'fvjxe': 66, 'pdigs': 32}


def func2():
    return 78.23


def func3():
    return 'citlx'


def func4():
    return (70, 81, 90)


def func5():
    return [44, 19, 95]


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
