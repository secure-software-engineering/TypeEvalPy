# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 75, 41)


def func2():
    return 'hmcau'


def func3():
    return {'dzzjs': 10, 'ijwhp': 19, 'hyqeu': 60}


def func4():
    return 32


def func5():
    return [80, 45, 79]


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
