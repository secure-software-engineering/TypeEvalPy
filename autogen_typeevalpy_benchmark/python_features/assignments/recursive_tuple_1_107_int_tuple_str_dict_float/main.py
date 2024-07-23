# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 74


def func2():
    return (84, 22, 24)


def func3():
    return 'hzzej'


def func4():
    return {'ltgqp': 79, 'tgtes': 19, 'yxqhc': 19}


def func5():
    return 74.15


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
