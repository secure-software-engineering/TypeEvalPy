# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cdfuw'


def func2():
    return {'gxysn': 8, 'kkohg': 56, 'qyruy': 52}


def func3():
    return 81.69


def func4():
    return 20


def func5():
    return (54, 61, 4)


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
