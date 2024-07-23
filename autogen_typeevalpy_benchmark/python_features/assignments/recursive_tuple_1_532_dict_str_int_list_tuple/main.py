# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nbmxf': 5, 'kjyri': 27, 'lpyeu': 62}


def func2():
    return 'fkvsj'


def func3():
    return 67


def func4():
    return [24, 35, 7]


def func5():
    return (25, 22, 37)


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
