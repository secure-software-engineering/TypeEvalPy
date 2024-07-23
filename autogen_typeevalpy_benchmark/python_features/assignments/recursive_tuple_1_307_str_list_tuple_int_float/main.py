# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ehlwj'


def func2():
    return [53, 21, 79]


def func3():
    return (77, 15, 53)


def func4():
    return 10


def func5():
    return 80.9


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
