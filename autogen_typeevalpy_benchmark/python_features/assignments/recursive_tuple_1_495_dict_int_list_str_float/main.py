# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ptgsw': 19, 'hlfww': 29, 'gnrro': 7}


def func2():
    return 76


def func3():
    return [43, 65, 54]


def func4():
    return 'dssfo'


def func5():
    return 81.94


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
