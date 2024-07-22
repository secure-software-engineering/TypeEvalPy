# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31.87


def func2():
    return 32


def func3():
    return 'hvatj'


def func4():
    return (55, 25, 10)


def func5():
    return [88, 53, 23]


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
