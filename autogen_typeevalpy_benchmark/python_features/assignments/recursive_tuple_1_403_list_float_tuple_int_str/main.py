# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [76, 96, 45]


def func2():
    return 66.74


def func3():
    return (12, 39, 26)


def func4():
    return 62


def func5():
    return 'hwnbv'


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
