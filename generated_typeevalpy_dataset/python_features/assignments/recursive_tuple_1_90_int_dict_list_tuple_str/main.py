# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 16


def func2():
    return {'fgufc': 33, 'qkslc': 40, 'nbyri': 51}


def func3():
    return [33, 17, 75]


def func4():
    return (10, 40, 12)


def func5():
    return 'uzbtq'


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
