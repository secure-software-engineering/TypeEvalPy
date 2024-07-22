# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15.24


def func2():
    return (100, 68, 95)


def func3():
    return 'ophjs'


def func4():
    return [75, 16, 21]


def func5():
    return {'iakot': 33, 'mahlm': 40, 'wyjco': 5}


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
