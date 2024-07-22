# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'uhlwu'


def func2():
    return 88


def func3():
    return (89, 72, 36)


def func4():
    return {'kzqfj': 92, 'feajj': 66, 'puhxy': 10}


def func5():
    return 85.99


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
