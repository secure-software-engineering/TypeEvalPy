# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [54, 50, 47]


def func2():
    return 27


def func3():
    return 96.17


def func4():
    return (79, 57, 4)


def func5():
    return {'jrcgf': 9, 'nawhg': 86, 'oaikw': 84}


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
