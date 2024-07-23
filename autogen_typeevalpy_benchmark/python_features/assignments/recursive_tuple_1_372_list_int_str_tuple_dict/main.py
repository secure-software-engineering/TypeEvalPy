# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [21, 9, 22]


def func2():
    return 76


def func3():
    return 'cjwmp'


def func4():
    return (79, 4, 22)


def func5():
    return {'ekuad': 50, 'gwyip': 92, 'pepvj': 58}


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
