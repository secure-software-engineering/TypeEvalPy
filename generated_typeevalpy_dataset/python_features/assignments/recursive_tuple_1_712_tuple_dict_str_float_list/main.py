# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (33, 30, 79)


def func2():
    return {'zsmhz': 58, 'ksjtq': 95, 'dndtk': 85}


def func3():
    return 'nbigm'


def func4():
    return 67.4


def func5():
    return [12, 27, 59]


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
