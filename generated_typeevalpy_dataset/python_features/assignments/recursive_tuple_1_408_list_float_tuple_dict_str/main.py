# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [11, 14, 27]


def func2():
    return 48.57


def func3():
    return (80, 80, 33)


def func4():
    return {'zmawu': 41, 'eqvwr': 16, 'yuygz': 7}


def func5():
    return 'fuwfx'


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
