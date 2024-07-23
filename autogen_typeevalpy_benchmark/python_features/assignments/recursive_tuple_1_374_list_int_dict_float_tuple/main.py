# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [93, 48, 94]


def func2():
    return 99


def func3():
    return {'ihcsv': 56, 'rsxnz': 87, 'kgwmy': 34}


def func4():
    return 71.49


def func5():
    return (36, 16, 72)


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
