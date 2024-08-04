# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cdsft'


def func2():
    return 9.03


def func3():
    return 12


def func4():
    return (92, 12, 1)


def func5():
    return {'lrfsk': 57, 'qfvsm': 24, 'smtpw': 65}


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
