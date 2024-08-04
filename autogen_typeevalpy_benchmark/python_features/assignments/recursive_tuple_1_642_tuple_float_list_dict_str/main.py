# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (86, 72, 59)


def func2():
    return 40.2


def func3():
    return [1, 48, 88]


def func4():
    return {'muzzs': 63, 'wucgw': 31, 'uceaj': 28}


def func5():
    return 'evrpm'


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
