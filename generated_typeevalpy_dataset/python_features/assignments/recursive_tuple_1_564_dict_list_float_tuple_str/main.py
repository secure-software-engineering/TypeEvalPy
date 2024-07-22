# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'peikw': 44, 'rgvwt': 10, 'txexj': 77}


def func2():
    return [22, 69, 8]


def func3():
    return 62.35


def func4():
    return (21, 93, 42)


def func5():
    return 'fwsys'


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
