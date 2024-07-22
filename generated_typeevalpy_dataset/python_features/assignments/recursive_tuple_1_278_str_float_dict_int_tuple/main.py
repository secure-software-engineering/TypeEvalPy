# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'junrh'


def func2():
    return 88.77


def func3():
    return {'uqbgk': 76, 'ckxcy': 48, 'cieza': 43}


def func4():
    return 73


def func5():
    return (17, 31, 24)


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
