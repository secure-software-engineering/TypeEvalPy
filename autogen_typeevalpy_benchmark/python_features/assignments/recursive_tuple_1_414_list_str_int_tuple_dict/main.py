# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [16, 19, 85]


def func2():
    return 'wqehy'


def func3():
    return 70


def func4():
    return (4, 74, 72)


def func5():
    return {'egsqr': 89, 'ermve': 69, 'vkase': 13}


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
