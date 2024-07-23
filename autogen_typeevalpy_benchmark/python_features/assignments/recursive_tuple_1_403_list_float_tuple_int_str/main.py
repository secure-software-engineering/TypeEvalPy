# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [53, 65, 44]


def func2():
    return 35.1


def func3():
    return (48, 50, 19)


def func4():
    return 83


def func5():
    return 'mslkq'


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
