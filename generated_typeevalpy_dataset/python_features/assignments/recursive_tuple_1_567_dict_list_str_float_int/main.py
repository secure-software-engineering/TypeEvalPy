# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ucwjs': 63, 'kkepz': 54, 'xkmpk': 77}


def func2():
    return [43, 49, 42]


def func3():
    return 'urlov'


def func4():
    return 60.12


def func5():
    return 64


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
