# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return 'rgbvu'


def func3():
    return 30.07


def func4():
    return [59, 72, 57]


def func5():
    return (78, 94, 46)


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
