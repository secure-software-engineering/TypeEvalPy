# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7.09


def func2():
    return [25, 98, 65]


def func3():
    return {'dgebp': 12, 'rkqvy': 73, 'iodmv': 60}


def func4():
    return (12, 15, 12)


def func5():
    return 'eciqa'


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
