# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (25, 99, 8)


def func2():
    return 90.12


def func3():
    return [55, 26, 21]


def func4():
    return 'cvyem'


def func5():
    return 22


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
