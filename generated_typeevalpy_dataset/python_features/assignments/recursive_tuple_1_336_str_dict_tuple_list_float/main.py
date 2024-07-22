# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'apqqh'


def func2():
    return {'iylzz': 96, 'roryc': 70, 'vvakb': 67}


def func3():
    return (96, 84, 57)


def func4():
    return [35, 86, 59]


def func5():
    return 73.36


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
