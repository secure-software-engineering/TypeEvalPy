# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yuirt': 4, 'kbmpm': 31, 'siewp': 68}


def func2():
    return (34, 19, 24)


def func3():
    return 62


def func4():
    return 21.8


def func5():
    return [52, 96, 17]


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
