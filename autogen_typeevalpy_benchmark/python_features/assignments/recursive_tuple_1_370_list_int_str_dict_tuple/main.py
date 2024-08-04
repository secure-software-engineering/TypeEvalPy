# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [72, 97, 3]


def func2():
    return 37


def func3():
    return 'vxyxd'


def func4():
    return {'dspio': 53, 'wdpjr': 81, 'lgujj': 10}


def func5():
    return (28, 2, 72)


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
