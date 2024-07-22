# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tonac': 75, 'astvw': 86, 'prbya': 18}


def func2():
    return 'tkgqx'


def func3():
    return [46, 40, 41]


def func4():
    return 46.19


def func5():
    return (51, 40, 82)


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
