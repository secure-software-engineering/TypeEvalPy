# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rhfpn'


def func2():
    return {'gjjks': 43, 'xlbtv': 35, 'aqbnm': 54}


def func3():
    return [64, 32, 42]


def func4():
    return 28


def func5():
    return (84, 10, 83)


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
