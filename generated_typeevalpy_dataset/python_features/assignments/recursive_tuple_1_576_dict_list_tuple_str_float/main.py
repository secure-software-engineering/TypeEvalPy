# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wrnnd': 81, 'suoep': 45, 'qxibj': 61}


def func2():
    return [92, 57, 90]


def func3():
    return (56, 81, 60)


def func4():
    return 'xvfcb'


def func5():
    return 27.57


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
