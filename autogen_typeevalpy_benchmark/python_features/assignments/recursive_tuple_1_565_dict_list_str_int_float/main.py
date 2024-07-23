# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'olmtu': 40, 'puegh': 58, 'nevye': 26}


def func2():
    return [81, 49, 79]


def func3():
    return 'byhwy'


def func4():
    return 45


def func5():
    return 95.22


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
