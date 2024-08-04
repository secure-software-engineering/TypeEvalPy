# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cbkuh': 10, 'varfo': 29, 'hdodx': 100}


def func2():
    return 50


def func3():
    return 'ernhk'


def func4():
    return 57.52


def func5():
    return [93, 61, 85]


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
