# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wcoac': 35, 'wqoes': 10, 'beolg': 99}


def func2():
    return (64, 22, 29)


def func3():
    return [35, 45, 55]


def func4():
    return 78.31


def func5():
    return 26


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
