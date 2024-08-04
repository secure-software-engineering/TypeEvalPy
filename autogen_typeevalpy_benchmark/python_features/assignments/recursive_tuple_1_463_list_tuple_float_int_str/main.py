# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [37, 87, 43]


def func2():
    return (59, 43, 97)


def func3():
    return 87.77


def func4():
    return 73


def func5():
    return 'ozlww'


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
