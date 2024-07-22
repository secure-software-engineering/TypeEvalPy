# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rrvtw': 58, 'ryfwr': 65, 'mdhkg': 56}


def func2():
    return 33


def func3():
    return [56, 28, 39]


def func4():
    return (18, 66, 19)


def func5():
    return 'dmpnn'


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
