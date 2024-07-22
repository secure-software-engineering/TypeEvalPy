# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lndgi': 62, 'vuwop': 90, 'ylaac': 34}


def func2():
    return 42.18


def func3():
    return (87, 44, 49)


def func4():
    return 68


def func5():
    return [79, 15, 91]


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
