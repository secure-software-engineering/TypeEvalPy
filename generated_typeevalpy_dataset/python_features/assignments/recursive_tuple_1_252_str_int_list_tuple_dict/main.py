# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kkkmx'


def func2():
    return 54


def func3():
    return [69, 99, 15]


def func4():
    return (27, 25, 22)


def func5():
    return {'lylil': 92, 'yxyyq': 96, 'xnpyf': 48}


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
