# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 74.99


def func2():
    return [95, 17, 40]


def func3():
    return (7, 49, 91)


def func4():
    return 37


def func5():
    return {'edife': 81, 'wehsg': 88, 'mpjql': 22}


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
