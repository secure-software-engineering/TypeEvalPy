# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kookw'


def func2():
    return 75


def func3():
    return 40.56


def func4():
    return {'oxkgu': 90, 'juljy': 32, 'gocsi': 69}


def func5():
    return [75, 17, 13]


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
