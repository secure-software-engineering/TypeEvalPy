# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xouuc': 58, 'nlxyv': 66, 'nwgrm': 99}


def func2():
    return 54


def func3():
    return [78, 91, 86]


def func4():
    return 'qbene'


def func5():
    return (22, 31, 97)


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
