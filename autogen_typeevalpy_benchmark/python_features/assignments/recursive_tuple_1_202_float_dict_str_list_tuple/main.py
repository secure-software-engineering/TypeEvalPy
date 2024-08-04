# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 42.12


def func2():
    return {'tthtz': 99, 'jnjyd': 100, 'kfchw': 95}


def func3():
    return 'zojfx'


def func4():
    return [36, 41, 99]


def func5():
    return (47, 81, 14)


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
