# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49


def func2():
    return {'ogxqj': 92, 'urkll': 30, 'jmhyn': 40}


def func3():
    return 63.93


def func4():
    return [12, 40, 53]


def func5():
    return (99, 41, 12)


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
