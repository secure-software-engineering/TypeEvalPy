# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return (71, 93, 70)


def func3():
    return 'zrdls'


def func4():
    return [9, 37, 64]


def func5():
    return 80.96


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
