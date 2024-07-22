# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 73


def func2():
    return (9, 82, 92)


def func3():
    return 3.4


def func4():
    return 'ytgfv'


def func5():
    return [45, 3, 63]


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
