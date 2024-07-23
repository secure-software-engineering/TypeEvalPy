# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [94, 93, 57]


def func2():
    return {'yqewh': 76, 'zdbsu': 14, 'zfgtb': 41}


def func3():
    return (73, 18, 58)


def func4():
    return 'fzuqm'


def func5():
    return 4.66


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
