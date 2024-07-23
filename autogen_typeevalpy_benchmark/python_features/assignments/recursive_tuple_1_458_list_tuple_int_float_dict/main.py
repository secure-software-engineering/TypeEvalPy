# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [78, 73, 70]


def func2():
    return (76, 91, 33)


def func3():
    return 30


def func4():
    return 19.9


def func5():
    return {'iiixe': 65, 'mgiht': 77, 'ustga': 58}


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
