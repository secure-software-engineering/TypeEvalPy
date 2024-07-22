# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 98.27


def func2():
    return 'inyyo'


def func3():
    return [30, 62, 6]


def func4():
    return (53, 64, 92)


def func5():
    return {'whnjo': 61, 'dhnwh': 95, 'vaygp': 91}


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
