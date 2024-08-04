# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lwzrd': 12, 'mzxnh': 73, 'latlr': 15}


def func2():
    return 'omqoc'


def func3():
    return (39, 6, 7)


def func4():
    return [52, 74, 95]


def func5():
    return 93


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
