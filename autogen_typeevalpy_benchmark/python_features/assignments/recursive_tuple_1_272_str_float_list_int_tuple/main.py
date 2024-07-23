# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lwldg'


def func2():
    return 61.12


def func3():
    return [16, 70, 45]


def func4():
    return 60


def func5():
    return (85, 89, 15)


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
