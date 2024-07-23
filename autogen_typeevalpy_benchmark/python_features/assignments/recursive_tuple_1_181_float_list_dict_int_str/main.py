# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.17


def func2():
    return [47, 92, 89]


def func3():
    return {'rjgsn': 84, 'jrxyw': 15, 'vcrrz': 23}


def func4():
    return 6


def func5():
    return 'jvyoe'


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
