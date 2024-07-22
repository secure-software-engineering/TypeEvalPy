# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96


def func2():
    return 'eskkf'


def func3():
    return {'pvqvw': 15, 'mxkws': 43, 'hiyyd': 82}


def func4():
    return (89, 27, 68)


def func5():
    return 17.69


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
