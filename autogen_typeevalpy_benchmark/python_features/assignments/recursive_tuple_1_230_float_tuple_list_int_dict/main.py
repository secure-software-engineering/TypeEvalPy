# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52.25


def func2():
    return (99, 66, 59)


def func3():
    return [51, 30, 44]


def func4():
    return 4


def func5():
    return {'pzznp': 74, 'slgte': 24, 'jocfy': 48}


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
