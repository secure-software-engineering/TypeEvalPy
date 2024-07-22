# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72.84


def func2():
    return {'qenvq': 44, 'xcrwo': 48, 'rhmtb': 47}


def func3():
    return 60


def func4():
    return (66, 15, 2)


def func5():
    return [79, 40, 11]


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
