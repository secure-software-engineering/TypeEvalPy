# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cjvzr': 99, 'uexec': 37, 'wkpam': 44}


def func2():
    return [34, 29, 59]


def func3():
    return (65, 43, 74)


def func4():
    return 79


def func5():
    return 46.44


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
