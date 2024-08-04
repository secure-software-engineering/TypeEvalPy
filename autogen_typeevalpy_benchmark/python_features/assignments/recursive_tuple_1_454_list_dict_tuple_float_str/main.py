# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [43, 7, 58]


def func2():
    return {'vyskl': 42, 'icyeo': 14, 'saayx': 6}


def func3():
    return (64, 81, 90)


def func4():
    return 31.64


def func5():
    return 'azcgy'


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
