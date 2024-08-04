# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (2, 95, 96)


def func2():
    return 38


def func3():
    return [85, 85, 19]


def func4():
    return 30.53


def func5():
    return {'rjkac': 32, 'yylge': 79, 'xokvs': 49}


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
