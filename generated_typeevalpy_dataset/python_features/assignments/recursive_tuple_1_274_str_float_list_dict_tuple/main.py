# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'xoxsw'


def func2():
    return 82.2


def func3():
    return [81, 96, 85]


def func4():
    return {'bxzbh': 78, 'dvtec': 1, 'mlujn': 69}


def func5():
    return (83, 15, 45)


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
