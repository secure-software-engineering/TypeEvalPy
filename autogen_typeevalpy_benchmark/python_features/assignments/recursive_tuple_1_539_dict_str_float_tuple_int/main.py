# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'judjg': 99, 'yprvx': 84, 'meaep': 49}


def func2():
    return 'kigec'


def func3():
    return 80.92


def func4():
    return (33, 9, 91)


def func5():
    return 88


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
