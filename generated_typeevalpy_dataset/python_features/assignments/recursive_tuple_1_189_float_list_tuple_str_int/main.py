# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90.1


def func2():
    return [75, 46, 100]


def func3():
    return (25, 49, 14)


def func4():
    return 'erheq'


def func5():
    return 54


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
