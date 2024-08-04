# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (90, 83, 42)


def func2():
    return {'mbruq': 27, 'egrkq': 43, 'rlkvq': 32}


def func3():
    return [18, 20, 26]


def func4():
    return 88


def func5():
    return 'mopbd'


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
