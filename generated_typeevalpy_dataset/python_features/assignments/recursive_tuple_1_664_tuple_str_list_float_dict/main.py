# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (12, 76, 5)


def func2():
    return 'juhdf'


def func3():
    return [18, 85, 69]


def func4():
    return 47.05


def func5():
    return {'seeni': 31, 'oyryx': 24, 'wehex': 80}


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
