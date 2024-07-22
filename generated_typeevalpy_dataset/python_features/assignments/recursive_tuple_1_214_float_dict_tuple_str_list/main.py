# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21.61


def func2():
    return {'opaye': 12, 'nzcmn': 90, 'itjca': 88}


def func3():
    return (20, 83, 81)


def func4():
    return 'viftc'


def func5():
    return [51, 94, 46]


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
