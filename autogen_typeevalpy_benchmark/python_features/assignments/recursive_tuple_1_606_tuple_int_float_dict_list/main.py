# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (73, 69, 21)


def func2():
    return 63


def func3():
    return 12.88


def func4():
    return {'eszuu': 4, 'gctxn': 27, 'vigkh': 92}


def func5():
    return [90, 76, 69]


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
