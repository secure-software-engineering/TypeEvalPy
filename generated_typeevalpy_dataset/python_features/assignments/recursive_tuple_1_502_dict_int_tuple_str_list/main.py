# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kbbus': 63, 'mwydq': 52, 'akmpy': 2}


def func2():
    return 5


def func3():
    return (53, 94, 11)


def func4():
    return 'atore'


def func5():
    return [20, 64, 21]


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
