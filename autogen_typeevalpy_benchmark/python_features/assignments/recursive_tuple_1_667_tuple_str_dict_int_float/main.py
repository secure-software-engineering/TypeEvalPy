# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (64, 61, 50)


def func2():
    return 'wlluf'


def func3():
    return {'mlwyf': 86, 'fhxln': 79, 'ikxii': 11}


def func4():
    return 84


def func5():
    return 1.41


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
