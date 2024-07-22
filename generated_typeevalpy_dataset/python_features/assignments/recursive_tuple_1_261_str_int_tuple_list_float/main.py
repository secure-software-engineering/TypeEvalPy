# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cqapy'


def func2():
    return 32


def func3():
    return (63, 59, 1)


def func4():
    return [85, 20, 78]


def func5():
    return 47.5


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
