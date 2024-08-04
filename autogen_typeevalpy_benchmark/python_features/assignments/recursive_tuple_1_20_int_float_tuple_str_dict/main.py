# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 81


def func2():
    return 22.06


def func3():
    return (66, 37, 6)


def func4():
    return 'enbcs'


def func5():
    return {'vszwf': 27, 'nuwyq': 59, 'zshri': 77}


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
