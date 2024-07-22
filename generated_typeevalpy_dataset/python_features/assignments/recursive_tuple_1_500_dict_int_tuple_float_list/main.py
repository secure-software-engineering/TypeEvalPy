# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'otwpc': 99, 'kzuoz': 13, 'ywcyf': 38}


def func2():
    return 7


def func3():
    return (7, 93, 77)


def func4():
    return 78.49


def func5():
    return [74, 2, 5]


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
