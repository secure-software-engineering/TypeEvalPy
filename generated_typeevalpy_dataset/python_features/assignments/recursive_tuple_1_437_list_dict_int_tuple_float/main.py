# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [75, 6, 18]


def func2():
    return {'submw': 90, 'hfjio': 90, 'wngro': 42}


def func3():
    return 36


def func4():
    return (47, 68, 3)


def func5():
    return 19.71


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
