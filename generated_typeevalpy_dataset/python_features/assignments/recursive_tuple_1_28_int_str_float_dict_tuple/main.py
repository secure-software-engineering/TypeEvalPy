# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 3


def func2():
    return 'oczri'


def func3():
    return 78.23


def func4():
    return {'yopnh': 67, 'oqoni': 10, 'gpkyo': 10}


def func5():
    return (14, 23, 26)


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
