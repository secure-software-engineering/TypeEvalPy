# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xmujz': 18, 'keyil': 71, 'acqzo': 90}


def func2():
    return [43, 14, 71]


def func3():
    return 15


def func4():
    return (88, 54, 9)


def func5():
    return 'quzia'


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
