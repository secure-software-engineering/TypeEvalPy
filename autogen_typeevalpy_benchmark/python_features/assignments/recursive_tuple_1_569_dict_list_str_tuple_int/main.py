# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mdfif': 46, 'lkwxa': 60, 'uorsj': 65}


def func2():
    return [5, 2, 22]


def func3():
    return 'qrhud'


def func4():
    return (51, 24, 21)


def func5():
    return 16


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
