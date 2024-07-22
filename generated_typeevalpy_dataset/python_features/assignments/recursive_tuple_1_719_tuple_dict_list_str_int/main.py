# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (89, 35, 97)


def func2():
    return {'jejci': 34, 'rnbfj': 38, 'pupyh': 14}


def func3():
    return [28, 61, 70]


def func4():
    return 'qymkc'


def func5():
    return 82


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
