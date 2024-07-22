# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'adjzd': 65, 'zzaeq': 52, 'wdrcp': 88}


def func2():
    return 93.06


def func3():
    return (29, 78, 78)


def func4():
    return [75, 99, 23]


def func5():
    return 'lcaqe'


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
