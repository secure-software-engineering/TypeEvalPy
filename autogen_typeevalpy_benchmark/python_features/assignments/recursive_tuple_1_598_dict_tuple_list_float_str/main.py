# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nkgoz': 23, 'ewujf': 26, 'vdobr': 67}


def func2():
    return (56, 94, 91)


def func3():
    return [35, 9, 84]


def func4():
    return 2.2


def func5():
    return 'ypfwq'


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
