# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 71.67


def func2():
    return {'hsohs': 19, 'reudp': 75, 'wgfwp': 2}


def func3():
    return [34, 47, 93]


def func4():
    return 'nwnmx'


def func5():
    return (45, 83, 20)


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
