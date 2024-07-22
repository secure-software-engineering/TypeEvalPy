# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return {'ccmzi': 46, 'omlco': 69, 'rvanu': 67}


def func3():
    return 'hxzgm'


def func4():
    return (96, 98, 1)


def func5():
    return [22, 42, 82]


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
