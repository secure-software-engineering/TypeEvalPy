# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66


def func2():
    return 'jtrcv'


def func3():
    return (49, 12, 30)


def func4():
    return {'haqgt': 59, 'rmisd': 12, 'bhesx': 3}


def func5():
    return [29, 52, 26]


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
