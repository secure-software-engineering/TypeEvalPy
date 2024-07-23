# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dkicy': 88, 'vuoto': 99, 'jivhe': 41}


def func2():
    return 82.75


def func3():
    return 'eldbk'


def func4():
    return (3, 78, 79)


def func5():
    return [41, 32, 61]


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
