# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [51, 50, 94]


def func2():
    return (77, 100, 65)


def func3():
    return {'julxd': 44, 'ehasa': 24, 'ivqyn': 98}


def func4():
    return 40.51


def func5():
    return 19


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
