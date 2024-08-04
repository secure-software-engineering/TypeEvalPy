# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vvvho': 13, 'qxlca': 35, 'iphzy': 27}


def func2():
    return 'ltezz'


def func3():
    return 14


def func4():
    return (11, 24, 93)


def func5():
    return [28, 82, 4]


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
