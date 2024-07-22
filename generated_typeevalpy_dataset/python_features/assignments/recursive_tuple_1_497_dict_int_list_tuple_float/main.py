# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mwjhx': 17, 'ngrek': 62, 'fxrxc': 90}


def func2():
    return 85


def func3():
    return [55, 76, 9]


def func4():
    return (95, 67, 47)


def func5():
    return 24.34


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
