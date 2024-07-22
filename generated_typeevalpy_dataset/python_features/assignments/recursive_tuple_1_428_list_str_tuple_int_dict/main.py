# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [45, 44, 61]


def func2():
    return 'wrijp'


def func3():
    return (82, 48, 86)


def func4():
    return 44


def func5():
    return {'cicmh': 28, 'crxvv': 25, 'nzofh': 10}


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
