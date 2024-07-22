# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34


def func2():
    return (17, 54, 61)


def func3():
    return [7, 32, 95]


def func4():
    return 79.13


def func5():
    return {'znwsl': 53, 'hirxo': 77, 'jnwjj': 34}


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
