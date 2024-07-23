# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [70, 21, 23]


def func2():
    return {'ndgqt': 5, 'flacn': 58, 'zgezk': 43}


def func3():
    return 40.84


def func4():
    return (75, 15, 7)


def func5():
    return 58


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
