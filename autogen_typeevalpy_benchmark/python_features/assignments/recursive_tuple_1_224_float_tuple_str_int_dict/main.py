# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 77.83


def func2():
    return (38, 76, 19)


def func3():
    return 'ubfho'


def func4():
    return 41


def func5():
    return {'owtvc': 87, 'ftveo': 39, 'siptx': 21}


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
