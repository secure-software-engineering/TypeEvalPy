# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (99, 76, 31)


def func2():
    return [24, 53, 95]


def func3():
    return 50.06


def func4():
    return 'yfxtb'


def func5():
    return {'sixxv': 41, 'iuhqg': 12, 'lubok': 5}


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
