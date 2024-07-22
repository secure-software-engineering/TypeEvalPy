# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sktbt'


def func2():
    return 27


def func3():
    return {'qthdt': 29, 'qcjfs': 14, 'qutln': 18}


def func4():
    return 26.79


def func5():
    return [73, 17, 30]


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
