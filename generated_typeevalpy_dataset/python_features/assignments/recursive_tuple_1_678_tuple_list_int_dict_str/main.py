# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (87, 33, 44)


def func2():
    return [89, 57, 95]


def func3():
    return 38


def func4():
    return {'zbbut': 6, 'ygzaz': 30, 'bzxtn': 100}


def func5():
    return 'ytoaj'


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
