# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [72, 71, 88]


def func2():
    return (51, 33, 44)


def func3():
    return {'uzuvd': 29, 'fxxac': 23, 'gydcf': 96}


def func4():
    return 58.94


def func5():
    return 'tiqpb'


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
