# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49


def func2():
    return {'snonk': 69, 'cxxwk': 25, 'dsfke': 67}


def func3():
    return 36.76


def func4():
    return [66, 95, 36]


def func5():
    return 'otujv'


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
