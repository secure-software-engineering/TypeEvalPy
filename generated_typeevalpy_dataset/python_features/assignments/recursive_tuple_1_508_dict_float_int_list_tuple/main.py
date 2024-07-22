# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'johfe': 81, 'dyeef': 52, 'qwdkw': 65}


def func2():
    return 56.15


def func3():
    return 90


def func4():
    return [61, 9, 93]


def func5():
    return (90, 19, 46)


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
