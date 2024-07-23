# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92.38


def func2():
    return {'yiwdl': 58, 'aqkzh': 65, 'rdwly': 66}


def func3():
    return 'jdrys'


def func4():
    return [20, 61, 9]


def func5():
    return (28, 62, 84)


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
