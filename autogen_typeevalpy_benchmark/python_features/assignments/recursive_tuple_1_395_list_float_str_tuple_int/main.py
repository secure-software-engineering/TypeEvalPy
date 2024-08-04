# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [17, 47, 66]


def func2():
    return 98.49


def func3():
    return 'sxhyb'


def func4():
    return (28, 23, 91)


def func5():
    return 70


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
