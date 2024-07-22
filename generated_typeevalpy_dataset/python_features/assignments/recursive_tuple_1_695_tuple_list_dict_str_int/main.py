# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (43, 78, 29)


def func2():
    return [52, 93, 15]


def func3():
    return {'jskbu': 93, 'kjcbf': 13, 'xwhfi': 29}


def func4():
    return 'qyntb'


def func5():
    return 49


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
