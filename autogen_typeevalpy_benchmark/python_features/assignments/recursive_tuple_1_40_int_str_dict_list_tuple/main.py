# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14


def func2():
    return 'izqhe'


def func3():
    return {'revpa': 53, 'fxkfh': 51, 'nljai': 21}


def func4():
    return [15, 17, 69]


def func5():
    return (54, 62, 96)


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
