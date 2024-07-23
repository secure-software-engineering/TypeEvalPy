# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qemtj': 51, 'lqqih': 32, 'afcho': 75}


def func2():
    return [64, 22, 32]


def func3():
    return 85


def func4():
    return (21, 96, 74)


def func5():
    return 14.81


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
