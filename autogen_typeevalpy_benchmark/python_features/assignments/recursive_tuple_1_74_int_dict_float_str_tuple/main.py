# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 83


def func2():
    return {'vpkdz': 43, 'lapcd': 100, 'cobqj': 35}


def func3():
    return 15.49


def func4():
    return 'uhczf'


def func5():
    return (14, 16, 23)


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
