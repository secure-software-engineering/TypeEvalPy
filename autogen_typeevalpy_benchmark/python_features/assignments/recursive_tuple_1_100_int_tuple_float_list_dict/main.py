# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return (77, 2, 97)


def func3():
    return 91.06


def func4():
    return [25, 71, 26]


def func5():
    return {'qagzo': 97, 'oubiy': 51, 'ajhkf': 93}


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
