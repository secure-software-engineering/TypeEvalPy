# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (15, 36, 53)


def func2():
    return 36.17


def func3():
    return {'aezay': 79, 'icvnn': 10, 'gmqfq': 6}


def func4():
    return 84


def func5():
    return [53, 57, 14]


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
