# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (78, 79, 46)


def func2():
    return 33


def func3():
    return 'lcmuc'


def func4():
    return 20.42


def func5():
    return [79, 82, 83]


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
