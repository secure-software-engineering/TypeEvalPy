# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'eprge'


def func2():
    return 65.94


def func3():
    return (92, 21, 76)


def func4():
    return {'jygif': 85, 'hgzga': 77, 'jzsgi': 81}


def func5():
    return 18


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
