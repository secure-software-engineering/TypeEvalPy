# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (45, 99, 74)


def func2():
    return [4, 15, 52]


def func3():
    return {'ugpta': 36, 'tfgzf': 69, 'xkmuy': 13}


def func4():
    return 'hvorc'


def func5():
    return 8


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
