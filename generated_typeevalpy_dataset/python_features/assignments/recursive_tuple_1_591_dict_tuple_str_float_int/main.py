# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bequu': 14, 'ggxep': 65, 'vqoal': 30}


def func2():
    return (51, 87, 69)


def func3():
    return 'hwowq'


def func4():
    return 52.48


def func5():
    return 43


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
