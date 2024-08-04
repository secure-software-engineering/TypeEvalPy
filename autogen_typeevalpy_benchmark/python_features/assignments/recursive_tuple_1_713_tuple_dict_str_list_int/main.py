# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 46, 1)


def func2():
    return {'ebcpc': 83, 'ggjfp': 44, 'cbbas': 56}


def func3():
    return 'cdvjs'


def func4():
    return [36, 90, 64]


def func5():
    return 9


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
