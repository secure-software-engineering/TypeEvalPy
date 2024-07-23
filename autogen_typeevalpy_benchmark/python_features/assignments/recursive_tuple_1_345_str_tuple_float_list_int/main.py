# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mtyhh'


def func2():
    return (35, 38, 75)


def func3():
    return 81.09


def func4():
    return [97, 69, 40]


def func5():
    return 24


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
