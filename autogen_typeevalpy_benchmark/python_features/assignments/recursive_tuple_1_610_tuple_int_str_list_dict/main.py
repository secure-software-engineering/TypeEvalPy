# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (44, 83, 68)


def func2():
    return 75


def func3():
    return 'wtxcq'


def func4():
    return [33, 99, 75]


def func5():
    return {'xrxrc': 27, 'ayucb': 4, 'peqbw': 66}


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
