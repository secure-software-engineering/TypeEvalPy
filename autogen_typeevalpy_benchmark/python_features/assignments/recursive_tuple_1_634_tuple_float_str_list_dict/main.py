# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (32, 95, 63)


def func2():
    return 60.32


def func3():
    return 'ybdao'


def func4():
    return [26, 99, 61]


def func5():
    return {'ssfay': 6, 'wwaws': 67, 'iemol': 10}


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
