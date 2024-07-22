# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [27, 3, 5]


def func2():
    return 42


def func3():
    return (37, 56, 33)


def func4():
    return 'xbpoi'


def func5():
    return {'uqqfl': 3, 'xeoio': 90, 'hpfbt': 54}


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
