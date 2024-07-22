# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pzvkn'


def func2():
    return [34, 27, 1]


def func3():
    return 44


def func4():
    return (91, 94, 12)


def func5():
    return {'keoer': 51, 'jerho': 27, 'ahhya': 62}


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
