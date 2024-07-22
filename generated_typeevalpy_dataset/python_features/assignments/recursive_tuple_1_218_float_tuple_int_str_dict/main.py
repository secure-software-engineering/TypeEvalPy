# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.61


def func2():
    return (31, 12, 9)


def func3():
    return 50


def func4():
    return 'juwev'


def func5():
    return {'zntmo': 31, 'fjvok': 98, 'joesp': 46}


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
