# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (29, 2, 16)


def func2():
    return 48.06


def func3():
    return {'cimua': 97, 'ifooa': 20, 'kixqf': 75}


def func4():
    return 'chiky'


def func5():
    return 89


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
