# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (93, 69, 15)


def func2():
    return 54


def func3():
    return 'mwaqy'


def func4():
    return [35, 85, 29]


def func5():
    return 68.1


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
