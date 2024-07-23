# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [65, 72, 10]


def func2():
    return 'zgwai'


def func3():
    return 61


def func4():
    return {'wcqha': 56, 'ihfzv': 57, 'wvwye': 21}


def func5():
    return 71.33


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
