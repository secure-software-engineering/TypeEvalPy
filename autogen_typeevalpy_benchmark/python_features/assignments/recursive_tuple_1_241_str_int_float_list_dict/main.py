# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'eqbcs'


def func2():
    return 85


def func3():
    return 41.06


def func4():
    return [34, 19, 92]


def func5():
    return {'ijdkv': 36, 'twupz': 4, 'ifvge': 64}


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
