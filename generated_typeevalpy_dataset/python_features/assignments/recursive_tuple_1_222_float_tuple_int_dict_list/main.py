# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62.97


def func2():
    return (44, 58, 52)


def func3():
    return 36


def func4():
    return {'dieif': 58, 'oansh': 40, 'ujmzn': 74}


def func5():
    return [40, 82, 32]


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
