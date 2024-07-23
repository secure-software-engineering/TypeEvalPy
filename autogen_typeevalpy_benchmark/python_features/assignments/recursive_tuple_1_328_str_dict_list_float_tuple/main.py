# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'zpfkw'


def func2():
    return {'zbbvp': 42, 'zwcxe': 56, 'siztd': 1}


def func3():
    return [35, 93, 46]


def func4():
    return 58.82


def func5():
    return (34, 7, 37)


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
