# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return [1, 2, 65]


def func3():
    return 73.31


def func4():
    return (48, 63, 52)


def func5():
    return {'yyzjm': 97, 'qpkbx': 93, 'koflg': 45}


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
