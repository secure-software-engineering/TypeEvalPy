# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (78, 60, 39)


def func2():
    return 27.1


def func3():
    return 3


def func4():
    return {'nnbtl': 12, 'bspmz': 70, 'pbrds': 93}


def func5():
    return [89, 81, 37]


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
