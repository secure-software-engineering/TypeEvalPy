# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jfwic': 53, 'xeiit': 60, 'psnko': 66}


def func2():
    return 'cuvix'


def func3():
    return [30, 89, 96]


def func4():
    return 56


def func5():
    return (61, 31, 18)


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
