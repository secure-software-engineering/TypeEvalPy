# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'suyuo'


def func2():
    return 54


def func3():
    return (85, 64, 75)


def func4():
    return 69.7


def func5():
    return [7, 41, 30]


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