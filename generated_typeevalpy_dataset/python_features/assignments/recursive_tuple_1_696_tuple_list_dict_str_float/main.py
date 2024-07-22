# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (15, 36, 82)


def func2():
    return [81, 69, 80]


def func3():
    return {'kefve': 95, 'gvfbs': 46, 'lkxvx': 44}


def func4():
    return 'trkhw'


def func5():
    return 54.61


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
