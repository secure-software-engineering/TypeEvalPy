# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jolqw': 9, 'wgkmr': 48, 'kgovz': 85}


def func2():
    return (39, 89, 12)


def func3():
    return [67, 48, 67]


def func4():
    return 'toydm'


def func5():
    return 69.88


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
