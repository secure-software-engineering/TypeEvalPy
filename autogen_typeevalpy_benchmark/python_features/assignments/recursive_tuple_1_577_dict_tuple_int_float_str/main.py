# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'psied': 93, 'eqyne': 31, 'ahtwk': 33}


def func2():
    return (75, 86, 51)


def func3():
    return 59


def func4():
    return 10.66


def func5():
    return 'pcezq'


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
