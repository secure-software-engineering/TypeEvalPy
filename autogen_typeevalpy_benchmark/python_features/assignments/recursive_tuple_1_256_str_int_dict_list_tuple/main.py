# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'feubj'


def func2():
    return 25


def func3():
    return {'dofew': 48, 'lukwk': 25, 'lsfpo': 71}


def func4():
    return [70, 12, 1]


def func5():
    return (3, 87, 99)


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
