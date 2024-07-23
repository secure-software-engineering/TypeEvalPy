# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (96, 80, 73)


def func2():
    return [97, 17, 21]


def func3():
    return 'kijnv'


def func4():
    return 33.43


def func5():
    return 81


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
