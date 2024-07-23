# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 43.46


def func2():
    return {'lhnqo': 69, 'ydcra': 33, 'mrygi': 62}


def func3():
    return [87, 90, 75]


def func4():
    return 9


def func5():
    return 'zpobm'


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
