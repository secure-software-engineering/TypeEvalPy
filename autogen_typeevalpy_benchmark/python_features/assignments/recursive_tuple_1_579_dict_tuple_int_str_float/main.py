# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fmlyo': 37, 'ucyre': 57, 'iryrl': 89}


def func2():
    return (47, 55, 17)


def func3():
    return 44


def func4():
    return 'iqdqw'


def func5():
    return 72.66


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
