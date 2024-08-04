# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (12, 43, 89)


def func2():
    return [23, 50, 52]


def func3():
    return 'jiwgt'


def func4():
    return {'keuwn': 57, 'qkhgu': 100, 'jgwse': 35}


def func5():
    return 98


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
