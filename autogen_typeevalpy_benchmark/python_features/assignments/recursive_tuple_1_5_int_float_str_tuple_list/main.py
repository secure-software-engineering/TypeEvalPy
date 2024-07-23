# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return 63.82


def func3():
    return 'duwmk'


def func4():
    return (92, 8, 95)


def func5():
    return [83, 25, 4]


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
