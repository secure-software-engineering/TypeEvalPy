# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [72, 12, 18]


def func2():
    return (77, 89, 90)


def func3():
    return 'yprft'


def func4():
    return 58


def func5():
    return 14.06


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
