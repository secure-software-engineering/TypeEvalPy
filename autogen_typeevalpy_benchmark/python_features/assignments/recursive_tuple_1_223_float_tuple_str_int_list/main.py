# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31.74


def func2():
    return (26, 11, 46)


def func3():
    return 'jwjbl'


def func4():
    return 69


def func5():
    return [47, 49, 38]


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
