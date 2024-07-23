# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47.03


def func2():
    return (49, 61, 73)


def func3():
    return {'jvhar': 26, 'jtnvs': 82, 'cfpho': 16}


def func4():
    return [8, 7, 45]


def func5():
    return 'mlclm'


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
