# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jugkb'


def func2():
    return {'uputf': 43, 'vvuul': 47, 'rgdez': 61}


def func3():
    return 59.95


def func4():
    return [81, 92, 44]


def func5():
    return (95, 85, 17)


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
