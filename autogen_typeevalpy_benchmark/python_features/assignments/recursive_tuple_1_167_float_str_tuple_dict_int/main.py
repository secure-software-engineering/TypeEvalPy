# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 16.52


def func2():
    return 'iltrb'


def func3():
    return (89, 41, 5)


def func4():
    return {'lyuiv': 20, 'rwaqa': 63, 'djyrg': 24}


def func5():
    return 94


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
