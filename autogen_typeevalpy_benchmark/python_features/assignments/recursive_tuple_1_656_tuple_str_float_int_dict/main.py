# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (69, 55, 3)


def func2():
    return 'ngimb'


def func3():
    return 7.29


def func4():
    return 3


def func5():
    return {'ykbqv': 4, 'gxnke': 78, 'uibpn': 100}


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
