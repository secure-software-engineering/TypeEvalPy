# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.64


def func2():
    return [75, 50, 20]


def func3():
    return (69, 73, 27)


def func4():
    return 'zlqrh'


def func5():
    return 44


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
