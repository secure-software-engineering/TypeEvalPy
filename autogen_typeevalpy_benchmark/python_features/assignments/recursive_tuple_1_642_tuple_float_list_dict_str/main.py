# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (14, 79, 42)


def func2():
    return 77.02


def func3():
    return [87, 97, 10]


def func4():
    return {'lttir': 96, 'qdcdc': 37, 'jlteg': 24}


def func5():
    return 'zcaeo'


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
