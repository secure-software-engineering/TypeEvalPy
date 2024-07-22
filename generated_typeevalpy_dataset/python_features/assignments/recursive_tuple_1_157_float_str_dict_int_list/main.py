# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 44.0


def func2():
    return 'bdyni'


def func3():
    return {'kygyi': 82, 'lzvfe': 39, 'sdlmh': 57}


def func4():
    return 39


def func5():
    return [81, 82, 81]


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
