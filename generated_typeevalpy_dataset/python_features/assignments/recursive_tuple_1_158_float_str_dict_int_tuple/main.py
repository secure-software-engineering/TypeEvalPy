# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49.75


def func2():
    return 'ygalk'


def func3():
    return {'jjykp': 50, 'odesb': 95, 'zsvsy': 11}


def func4():
    return 53


def func5():
    return (30, 67, 16)


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
