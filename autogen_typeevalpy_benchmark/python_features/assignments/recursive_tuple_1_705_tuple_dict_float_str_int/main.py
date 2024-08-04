# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (41, 25, 41)


def func2():
    return {'zyyeq': 77, 'pyayh': 98, 'qyjmz': 60}


def func3():
    return 52.89


def func4():
    return 'ayabx'


def func5():
    return 14


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
