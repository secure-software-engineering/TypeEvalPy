# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [83, 48, 79]


def func2():
    return 93


def func3():
    return 13.29


def func4():
    return (14, 86, 48)


def func5():
    return {'lspbj': 97, 'osuhe': 77, 'azzpe': 91}


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
