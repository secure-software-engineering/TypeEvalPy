# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sfwdl'


def func2():
    return [72, 26, 36]


def func3():
    return 28.06


def func4():
    return 7


def func5():
    return {'drwao': 99, 'gjwuk': 17, 'hssaz': 78}


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
