# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ktenv': 58, 'uwdmo': 64, 'itwdu': 43}


def func2():
    return [13, 18, 30]


def func3():
    return (76, 48, 98)


def func4():
    return 56.72


def func5():
    return 65


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
