# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'igdha'


def func2():
    return 60.73


def func3():
    return (84, 86, 66)


def func4():
    return 99


def func5():
    return {'kebut': 81, 'wfotv': 30, 'rxvjb': 73}


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
