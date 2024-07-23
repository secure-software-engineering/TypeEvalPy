# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (91, 40, 85)


def func2():
    return 'pfvqb'


def func3():
    return 58.16


def func4():
    return 65


def func5():
    return [14, 11, 8]


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
