# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wqiju': 22, 'koewa': 97, 'cesrq': 39}


def func2():
    return (58, 23, 71)


def func3():
    return 'kpgea'


def func4():
    return 85.26


def func5():
    return [22, 21, 32]


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
