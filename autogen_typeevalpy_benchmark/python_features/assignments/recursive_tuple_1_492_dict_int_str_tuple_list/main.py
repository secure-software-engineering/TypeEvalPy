# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'akoki': 45, 'rlkop': 55, 'yxcvk': 89}


def func2():
    return 5


def func3():
    return 'giagi'


def func4():
    return (29, 61, 26)


def func5():
    return [5, 76, 95]


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
