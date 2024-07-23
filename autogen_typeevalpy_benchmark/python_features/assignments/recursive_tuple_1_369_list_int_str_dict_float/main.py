# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [85, 28, 57]


def func2():
    return 64


def func3():
    return 'edpcy'


def func4():
    return {'viqzi': 85, 'npvid': 65, 'npths': 49}


def func5():
    return 21.03


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
