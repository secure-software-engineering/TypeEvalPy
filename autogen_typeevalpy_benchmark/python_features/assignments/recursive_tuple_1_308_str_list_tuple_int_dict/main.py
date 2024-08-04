# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gkgpx'


def func2():
    return [29, 36, 14]


def func3():
    return (1, 31, 86)


def func4():
    return 40


def func5():
    return {'lwwlg': 87, 'wkldx': 63, 'wtatf': 56}


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
