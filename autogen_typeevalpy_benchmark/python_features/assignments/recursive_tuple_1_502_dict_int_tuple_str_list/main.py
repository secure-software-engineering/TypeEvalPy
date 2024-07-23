# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wcbfm': 37, 'buzax': 69, 'isoft': 70}


def func2():
    return 76


def func3():
    return (96, 22, 61)


def func4():
    return 'bkyqy'


def func5():
    return [67, 47, 100]


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
