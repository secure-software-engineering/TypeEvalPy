# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 86.44


def func2():
    return [80, 49, 41]


def func3():
    return 'oljub'


def func4():
    return (37, 77, 70)


def func5():
    return {'jrwsl': 41, 'fiinx': 73, 'jeacd': 11}


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
