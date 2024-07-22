# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 100, 47]


def func2():
    return (26, 20, 89)


def func3():
    return {'glugq': 82, 'phusg': 44, 'wmxiz': 97}


def func4():
    return 62


def func5():
    return 52.2


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
