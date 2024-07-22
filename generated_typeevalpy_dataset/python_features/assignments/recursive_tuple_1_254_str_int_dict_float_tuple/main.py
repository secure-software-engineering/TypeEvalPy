# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vubbf'


def func2():
    return 15


def func3():
    return {'zzawe': 27, 'uzmqx': 34, 'zxxgz': 32}


def func4():
    return 77.44


def func5():
    return (64, 45, 76)


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
