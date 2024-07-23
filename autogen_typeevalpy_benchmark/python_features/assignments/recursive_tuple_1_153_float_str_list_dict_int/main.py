# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.79


def func2():
    return 'avdse'


def func3():
    return [69, 42, 59]


def func4():
    return {'zevhm': 100, 'budmu': 49, 'azoat': 20}


def func5():
    return 73


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
