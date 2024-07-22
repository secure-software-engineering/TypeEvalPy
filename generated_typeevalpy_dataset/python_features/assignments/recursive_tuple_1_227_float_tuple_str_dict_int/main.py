# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82.49


def func2():
    return (5, 95, 18)


def func3():
    return 'cppjv'


def func4():
    return {'jetor': 22, 'afakt': 73, 'wuitr': 76}


def func5():
    return 1


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
