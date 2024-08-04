# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'sevcw': 70, 'cvujh': 54, 'rwsnw': 69}


def func2():
    return 50.45


def func3():
    return 'kxcpn'


def func4():
    return 34


def func5():
    return [72, 69, 8]


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
