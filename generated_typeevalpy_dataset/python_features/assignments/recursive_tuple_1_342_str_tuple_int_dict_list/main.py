# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tfpxl'


def func2():
    return (57, 96, 17)


def func3():
    return 23


def func4():
    return {'voqmn': 88, 'msfmr': 48, 'xfzlw': 2}


def func5():
    return [92, 99, 3]


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
