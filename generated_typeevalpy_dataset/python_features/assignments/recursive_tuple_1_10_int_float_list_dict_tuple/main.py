# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35


def func2():
    return 47.51


def func3():
    return [74, 42, 22]


def func4():
    return {'lifuy': 79, 'jybnq': 38, 'ukakq': 9}


def func5():
    return (13, 3, 96)


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
