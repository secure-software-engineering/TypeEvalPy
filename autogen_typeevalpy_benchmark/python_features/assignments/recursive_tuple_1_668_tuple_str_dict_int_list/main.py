# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 63, 42)


def func2():
    return 'lpwuw'


def func3():
    return {'zejlu': 99, 'lttvr': 41, 'wciqr': 57}


def func4():
    return 87


def func5():
    return [5, 46, 17]


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
