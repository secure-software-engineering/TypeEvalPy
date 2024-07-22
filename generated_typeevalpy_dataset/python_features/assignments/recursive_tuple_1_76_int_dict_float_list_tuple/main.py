# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return {'flxrz': 62, 'bqoak': 59, 'nqarb': 36}


def func3():
    return 73.49


def func4():
    return [84, 93, 48]


def func5():
    return (85, 17, 14)


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
