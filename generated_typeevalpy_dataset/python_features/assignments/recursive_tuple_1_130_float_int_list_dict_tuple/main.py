# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.06


def func2():
    return 48


def func3():
    return [75, 70, 54]


def func4():
    return {'xqtgq': 68, 'ooziw': 34, 'zwbya': 57}


def func5():
    return (99, 38, 88)


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
