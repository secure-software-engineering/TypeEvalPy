# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (1, 13, 84)


def func2():
    return 50.31


def func3():
    return 'kjoal'


def func4():
    return 25


def func5():
    return {'lwgax': 78, 'rvoqy': 62, 'fduoo': 42}


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
