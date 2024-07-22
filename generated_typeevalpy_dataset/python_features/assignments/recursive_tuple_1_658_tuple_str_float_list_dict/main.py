# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (43, 35, 20)


def func2():
    return 'yupgo'


def func3():
    return 45.54


def func4():
    return [21, 23, 3]


def func5():
    return {'tjtph': 73, 'dipip': 75, 'pdoet': 62}


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
