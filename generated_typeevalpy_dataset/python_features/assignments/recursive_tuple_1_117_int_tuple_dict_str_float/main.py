# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 2


def func2():
    return (5, 4, 40)


def func3():
    return {'colve': 77, 'aynhk': 92, 'tjnaa': 73}


def func4():
    return 'safwj'


def func5():
    return 29.24


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
