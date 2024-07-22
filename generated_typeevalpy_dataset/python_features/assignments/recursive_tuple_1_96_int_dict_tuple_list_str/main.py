# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6


def func2():
    return {'cajgl': 99, 'whdoq': 76, 'pwzxl': 38}


def func3():
    return (72, 74, 57)


def func4():
    return [15, 61, 43]


def func5():
    return 'qipbm'


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
