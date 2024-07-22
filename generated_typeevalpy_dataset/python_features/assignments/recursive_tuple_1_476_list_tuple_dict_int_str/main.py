# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [20, 12, 70]


def func2():
    return (55, 77, 65)


def func3():
    return {'emzmr': 34, 'xwjsf': 12, 'fexzk': 4}


def func4():
    return 79


def func5():
    return 'apute'


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
