# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (22, 48, 58)


def func2():
    return {'bzfrq': 36, 'ipjyw': 3, 'invnf': 18}


def func3():
    return 'pkxrp'


def func4():
    return 44.82


def func5():
    return 13


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
