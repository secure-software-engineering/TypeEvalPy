# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7


def func2():
    return [73, 36, 21]


def func3():
    return 69.94


def func4():
    return {'tkown': 68, 'eruav': 31, 'mvzcj': 75}


def func5():
    return (96, 69, 65)


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
