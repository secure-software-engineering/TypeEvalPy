# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (40, 30, 37)


def func2():
    return 87


def func3():
    return {'loyqz': 67, 'joqmc': 9, 'wixbi': 98}


def func4():
    return 'ixpzj'


def func5():
    return 51.88


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
