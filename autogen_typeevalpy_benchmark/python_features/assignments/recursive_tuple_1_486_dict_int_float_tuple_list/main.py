# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dhnry': 32, 'fwzur': 48, 'yttze': 83}


def func2():
    return 64


def func3():
    return 65.52


def func4():
    return (31, 38, 44)


def func5():
    return [21, 15, 40]


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
