# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hhgzf': 71, 'rypnq': 26, 'dyurk': 20}


def func2():
    return 'nedrn'


def func3():
    return [48, 57, 54]


def func4():
    return 23


def func5():
    return 7.75


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
