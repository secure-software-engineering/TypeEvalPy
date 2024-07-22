# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63.73


def func2():
    return 94


def func3():
    return 'knkms'


def func4():
    return [35, 26, 62]


def func5():
    return {'modfs': 29, 'fbfsf': 63, 'jtkxa': 13}


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
