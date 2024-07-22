# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'czovj'


def func2():
    return {'aqmfb': 5, 'huvuv': 45, 'ltwxe': 97}


def func3():
    return (51, 12, 61)


def func4():
    return 46


def func5():
    return 18.44


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
