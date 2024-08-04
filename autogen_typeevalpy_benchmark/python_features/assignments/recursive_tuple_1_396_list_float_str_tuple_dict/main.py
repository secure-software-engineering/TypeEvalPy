# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [14, 95, 18]


def func2():
    return 19.85


def func3():
    return 'bfdva'


def func4():
    return (40, 80, 12)


def func5():
    return {'btxnk': 24, 'mfoin': 45, 'tksre': 62}


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
