# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return {'uoyuj': 39, 'gubgx': 97, 'rufgb': 24}


def func3():
    return [22, 27, 49]


def func4():
    return 9.46


def func5():
    return (19, 70, 75)


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
