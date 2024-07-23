# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lhieb'


def func2():
    return (71, 93, 91)


def func3():
    return 63.0


def func4():
    return 83


def func5():
    return [55, 33, 77]


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
