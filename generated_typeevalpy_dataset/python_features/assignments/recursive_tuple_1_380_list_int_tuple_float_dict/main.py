# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [94, 21, 16]


def func2():
    return 88


def func3():
    return (94, 37, 40)


def func4():
    return 82.66


def func5():
    return {'hkliy': 81, 'jhdbn': 1, 'zdxkv': 22}


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
