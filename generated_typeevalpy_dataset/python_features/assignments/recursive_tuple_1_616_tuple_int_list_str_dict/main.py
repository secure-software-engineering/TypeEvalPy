# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (65, 87, 64)


def func2():
    return 59


def func3():
    return [42, 17, 79]


def func4():
    return 'mqyfl'


def func5():
    return {'zwvka': 85, 'pfrpo': 30, 'jczpw': 82}


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
