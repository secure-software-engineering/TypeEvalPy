# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [33, 90, 84]


def func2():
    return {'cnuoi': 33, 'hvdom': 36, 'powkd': 61}


def func3():
    return (99, 15, 53)


def func4():
    return 94


def func5():
    return 9.72


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
