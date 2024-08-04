# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (23, 96, 43)


def func2():
    return [44, 9, 94]


def func3():
    return 72.48


def func4():
    return 27


def func5():
    return {'vuhhr': 47, 'wkdnn': 36, 'ohtyb': 49}


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
