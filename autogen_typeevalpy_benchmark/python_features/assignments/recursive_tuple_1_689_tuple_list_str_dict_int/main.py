# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (86, 73, 91)


def func2():
    return [41, 46, 50]


def func3():
    return 'ttebn'


def func4():
    return {'pyqyg': 33, 'agblc': 7, 'cdtzq': 83}


def func5():
    return 31


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
