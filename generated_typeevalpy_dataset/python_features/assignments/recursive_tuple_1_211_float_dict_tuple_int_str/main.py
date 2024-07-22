# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 29.85


def func2():
    return {'pjljy': 55, 'efazv': 39, 'lukvd': 6}


def func3():
    return (81, 77, 70)


def func4():
    return 72


def func5():
    return 'frxqs'


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
