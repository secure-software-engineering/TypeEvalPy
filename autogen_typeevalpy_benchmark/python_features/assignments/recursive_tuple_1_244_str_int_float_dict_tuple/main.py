# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'asoqw'


def func2():
    return 69


def func3():
    return 71.28


def func4():
    return {'jjrpz': 61, 'wsfik': 5, 'cjbfm': 83}


def func5():
    return (76, 5, 79)


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
