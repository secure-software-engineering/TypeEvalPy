# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 21, 75]


def func2():
    return (96, 68, 28)


def func3():
    return 'dugvt'


def func4():
    return 82.3


def func5():
    return {'bkeou': 59, 'fdmnj': 97, 'ojvvx': 6}


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
