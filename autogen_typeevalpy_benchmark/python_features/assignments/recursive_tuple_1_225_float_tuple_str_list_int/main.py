# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.69


def func2():
    return (94, 74, 83)


def func3():
    return 'zzfbc'


def func4():
    return [7, 61, 41]


def func5():
    return 67


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
