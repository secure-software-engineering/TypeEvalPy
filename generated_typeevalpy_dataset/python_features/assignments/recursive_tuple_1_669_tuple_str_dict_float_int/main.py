# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (80, 81, 93)


def func2():
    return 'sysel'


def func3():
    return {'oevtb': 11, 'quunk': 51, 'hlhiu': 81}


def func4():
    return 48.09


def func5():
    return 1


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
