# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36


def func2():
    return 'gophp'


def func3():
    return 10.52


def func4():
    return (68, 26, 3)


def func5():
    return [10, 18, 21]


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
