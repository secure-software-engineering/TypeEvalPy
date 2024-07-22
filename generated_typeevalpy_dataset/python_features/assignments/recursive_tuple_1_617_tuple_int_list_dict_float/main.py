# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (22, 71, 76)


def func2():
    return 13


def func3():
    return [59, 66, 57]


def func4():
    return {'tivve': 3, 'wzxth': 56, 'jccvq': 49}


def func5():
    return 45.26


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
