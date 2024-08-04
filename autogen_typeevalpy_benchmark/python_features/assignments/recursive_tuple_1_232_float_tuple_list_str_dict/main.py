# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 3.52


def func2():
    return (70, 17, 13)


def func3():
    return [30, 59, 15]


def func4():
    return 'dsdjl'


def func5():
    return {'oyzze': 73, 'vxndr': 68, 'uftnu': 68}


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
