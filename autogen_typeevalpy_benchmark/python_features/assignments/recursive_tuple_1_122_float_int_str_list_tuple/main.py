# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75.62


def func2():
    return 52


def func3():
    return 'cumbh'


def func4():
    return [59, 64, 83]


def func5():
    return (16, 48, 80)


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
