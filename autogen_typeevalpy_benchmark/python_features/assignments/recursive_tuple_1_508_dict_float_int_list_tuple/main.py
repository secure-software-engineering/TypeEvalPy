# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'eeoyd': 73, 'cvnlk': 40, 'pqldp': 51}


def func2():
    return 42.2


def func3():
    return 19


def func4():
    return [96, 5, 88]


def func5():
    return (50, 47, 92)


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
