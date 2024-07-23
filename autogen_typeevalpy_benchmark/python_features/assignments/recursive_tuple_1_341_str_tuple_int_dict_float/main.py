# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sbswu'


def func2():
    return (72, 25, 55)


def func3():
    return 97


def func4():
    return {'wdppr': 100, 'xluqq': 46, 'amokh': 56}


def func5():
    return 31.48


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
