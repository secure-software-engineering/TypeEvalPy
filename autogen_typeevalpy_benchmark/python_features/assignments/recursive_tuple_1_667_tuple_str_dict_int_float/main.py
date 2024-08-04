# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (4, 84, 63)


def func2():
    return 'akswp'


def func3():
    return {'wbpfu': 59, 'pdoxf': 6, 'xnylh': 32}


def func4():
    return 92


def func5():
    return 32.3


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
