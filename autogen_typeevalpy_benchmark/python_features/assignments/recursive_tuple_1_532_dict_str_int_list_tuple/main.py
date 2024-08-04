# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xbppa': 13, 'abpif': 91, 'axvri': 11}


def func2():
    return 'oknxe'


def func3():
    return 38


def func4():
    return [50, 36, 95]


def func5():
    return (66, 100, 67)


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
