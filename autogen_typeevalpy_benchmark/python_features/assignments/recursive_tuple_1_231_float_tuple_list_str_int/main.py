# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26.27


def func2():
    return (63, 99, 71)


def func3():
    return [59, 85, 13]


def func4():
    return 'rinbj'


def func5():
    return 83


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
