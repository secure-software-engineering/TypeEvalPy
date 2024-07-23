# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [94, 10, 69]


def func2():
    return 40


def func3():
    return 85.61


def func4():
    return 'bvogy'


def func5():
    return {'vmsve': 63, 'jwkaw': 97, 'fuqao': 55}


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
