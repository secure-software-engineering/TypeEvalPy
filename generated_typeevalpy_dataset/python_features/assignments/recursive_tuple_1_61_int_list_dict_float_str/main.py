# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 33


def func2():
    return [91, 52, 4]


def func3():
    return {'uhmuf': 97, 'uxhla': 71, 'cxgsz': 10}


def func4():
    return 68.78


def func5():
    return 'qxhxe'


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
