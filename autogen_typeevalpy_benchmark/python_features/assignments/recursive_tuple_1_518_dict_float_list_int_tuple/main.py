# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jinou': 17, 'nxlid': 20, 'ekyzw': 4}


def func2():
    return 60.97


def func3():
    return [48, 45, 71]


def func4():
    return 77


def func5():
    return (37, 34, 38)


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
