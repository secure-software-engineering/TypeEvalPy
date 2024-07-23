# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mbbgf': 8, 'kehtp': 95, 'ffnua': 68}


def func2():
    return [35, 67, 94]


def func3():
    return 'rgzuu'


def func4():
    return (91, 36, 33)


def func5():
    return 75.03


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
