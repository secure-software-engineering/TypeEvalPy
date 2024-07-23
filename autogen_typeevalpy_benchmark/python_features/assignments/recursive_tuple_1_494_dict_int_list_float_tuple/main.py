# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'negby': 17, 'woxbn': 33, 'pzaav': 33}


def func2():
    return 55


def func3():
    return [2, 23, 53]


def func4():
    return 28.89


def func5():
    return (89, 64, 91)


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
