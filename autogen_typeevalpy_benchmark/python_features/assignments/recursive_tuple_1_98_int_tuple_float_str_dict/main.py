# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 59


def func2():
    return (71, 92, 34)


def func3():
    return 92.0


def func4():
    return 'nslez'


def func5():
    return {'nzdfq': 22, 'fetov': 7, 'vmiqv': 48}


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
