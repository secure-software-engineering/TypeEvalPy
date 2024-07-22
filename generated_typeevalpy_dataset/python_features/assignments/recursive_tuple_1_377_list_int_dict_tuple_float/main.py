# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [75, 80, 99]


def func2():
    return 81


def func3():
    return {'phiqm': 43, 'fiuvo': 99, 'kbrmh': 53}


def func4():
    return (72, 68, 64)


def func5():
    return 59.58


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
