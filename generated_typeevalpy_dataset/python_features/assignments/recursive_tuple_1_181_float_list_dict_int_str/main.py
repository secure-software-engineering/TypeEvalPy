# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 83.27


def func2():
    return [32, 20, 4]


def func3():
    return {'ymluy': 71, 'bxtxr': 54, 'beeno': 83}


def func4():
    return 84


def func5():
    return 'cqhov'


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
