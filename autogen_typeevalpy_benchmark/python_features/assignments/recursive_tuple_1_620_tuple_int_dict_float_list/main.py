# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (7, 84, 85)


def func2():
    return 90


def func3():
    return {'mkvsy': 67, 'yhqfa': 74, 'hybha': 64}


def func4():
    return 32.82


def func5():
    return [82, 70, 61]


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
