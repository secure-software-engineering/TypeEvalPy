# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 46


def func2():
    return (17, 90, 87)


def func3():
    return 10.64


def func4():
    return {'ktcud': 28, 'pjpwh': 88, 'dmxcs': 84}


def func5():
    return 'dsznz'


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
