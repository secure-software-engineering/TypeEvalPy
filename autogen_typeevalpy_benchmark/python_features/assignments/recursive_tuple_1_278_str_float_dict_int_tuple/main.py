# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kfusj'


def func2():
    return 78.0


def func3():
    return {'mfajq': 78, 'ouymi': 16, 'wfvey': 38}


def func4():
    return 94


def func5():
    return (8, 95, 25)


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
