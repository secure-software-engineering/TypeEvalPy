# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (27, 36, 40)


def func2():
    return {'adwwh': 72, 'frugn': 17, 'kiova': 23}


def func3():
    return 77


def func4():
    return 73.76


def func5():
    return [72, 44, 21]


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
