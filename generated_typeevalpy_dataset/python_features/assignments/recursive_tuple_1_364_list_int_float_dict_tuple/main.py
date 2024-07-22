# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [50, 42, 9]


def func2():
    return 70


def func3():
    return 51.63


def func4():
    return {'shvof': 69, 'lafpg': 30, 'xhczs': 88}


def func5():
    return (4, 38, 17)


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
