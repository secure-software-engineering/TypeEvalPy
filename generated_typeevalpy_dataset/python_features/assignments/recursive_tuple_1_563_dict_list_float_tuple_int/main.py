# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qtfwi': 52, 'kqfjz': 29, 'ahobh': 15}


def func2():
    return [14, 95, 91]


def func3():
    return 4.26


def func4():
    return (23, 17, 6)


def func5():
    return 57


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
