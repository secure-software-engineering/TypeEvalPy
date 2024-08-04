# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8.37


def func2():
    return {'esypy': 44, 'yukys': 36, 'gzpbb': 69}


def func3():
    return (48, 57, 37)


def func4():
    return [15, 61, 18]


def func5():
    return 'wbztv'


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
