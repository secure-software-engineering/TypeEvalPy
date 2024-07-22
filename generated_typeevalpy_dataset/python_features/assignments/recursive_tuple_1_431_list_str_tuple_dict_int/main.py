# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [36, 98, 13]


def func2():
    return 'rhvdz'


def func3():
    return (73, 96, 58)


def func4():
    return {'njwfw': 51, 'ajrav': 20, 'sugyn': 63}


def func5():
    return 53


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
