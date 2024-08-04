# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [69, 65, 81]


def func2():
    return 'phrav'


def func3():
    return 7.99


def func4():
    return (70, 52, 34)


def func5():
    return {'hdtlw': 34, 'jnyol': 70, 'nlaev': 6}


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
