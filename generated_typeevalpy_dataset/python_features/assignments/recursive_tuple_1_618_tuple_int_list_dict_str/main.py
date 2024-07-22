# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (23, 21, 71)


def func2():
    return 44


def func3():
    return [16, 1, 23]


def func4():
    return {'buiih': 55, 'mhovu': 32, 'qsuud': 80}


def func5():
    return 'htfpm'


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
