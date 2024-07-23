# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [59, 85, 38]


def func2():
    return 69.37


def func3():
    return (20, 33, 79)


def func4():
    return {'pgdyq': 92, 'oybqq': 42, 'wmzak': 46}


def func5():
    return 'ewfuz'


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
