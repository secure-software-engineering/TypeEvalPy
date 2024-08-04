# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 77


def func2():
    return 'mzsux'


def func3():
    return (73, 22, 33)


def func4():
    return {'ypzsr': 75, 'zsiqw': 58, 'iwmip': 49}


def func5():
    return [66, 82, 95]


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
