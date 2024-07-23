# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49


def func2():
    return [90, 7, 57]


def func3():
    return 'zqssk'


def func4():
    return (42, 66, 22)


def func5():
    return {'rvulo': 44, 'wukeg': 17, 'icbcp': 80}


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
