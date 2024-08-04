# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (36, 96, 9)


def func2():
    return 'frauq'


def func3():
    return 82.54


def func4():
    return [61, 77, 63]


def func5():
    return 74


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
