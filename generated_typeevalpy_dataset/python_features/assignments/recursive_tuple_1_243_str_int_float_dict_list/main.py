# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'snfda'


def func2():
    return 24


def func3():
    return 67.41


def func4():
    return {'iqpzg': 62, 'mmbna': 89, 'cvhzx': 27}


def func5():
    return [39, 64, 4]


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
