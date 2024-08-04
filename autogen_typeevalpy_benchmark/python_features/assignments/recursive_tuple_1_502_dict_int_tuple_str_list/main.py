# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'llupj': 72, 'vgteq': 99, 'fcxxt': 34}


def func2():
    return 63


def func3():
    return (22, 31, 4)


def func4():
    return 'fsydd'


def func5():
    return [38, 59, 9]


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
