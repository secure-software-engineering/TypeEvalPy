# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [93, 57, 37]


def func2():
    return (24, 43, 89)


def func3():
    return 30.11


def func4():
    return 77


def func5():
    return 'nxdii'


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
