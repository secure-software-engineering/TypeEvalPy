# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qvihy'


def func2():
    return [58, 51, 88]


def func3():
    return 51


def func4():
    return {'dooyq': 76, 'nwdra': 52, 'hgjnz': 51}


def func5():
    return (98, 81, 34)


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
