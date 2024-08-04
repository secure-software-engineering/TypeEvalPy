# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [45, 18, 8]


def func2():
    return 10


def func3():
    return 31.81


def func4():
    return 'bdnuh'


def func5():
    return {'ofkmv': 43, 'ptkes': 44, 'ypnbl': 54}


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
