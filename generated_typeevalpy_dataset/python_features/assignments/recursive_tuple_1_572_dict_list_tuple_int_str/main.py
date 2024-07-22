# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'naicy': 17, 'opapm': 8, 'hsoty': 20}


def func2():
    return [93, 4, 19]


def func3():
    return (18, 39, 23)


def func4():
    return 5


def func5():
    return 'admhd'


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
