# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89


def func2():
    return (20, 57, 7)


def func3():
    return {'ekkax': 56, 'dkbet': 81, 'redyh': 85}


def func4():
    return 'eudwm'


def func5():
    return 45.86


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
