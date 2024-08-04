# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dwjgl': 28, 'orinc': 92, 'ndhbd': 60}


def func2():
    return 'fbisu'


def func3():
    return 50.12


def func4():
    return [49, 97, 52]


def func5():
    return 18


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
