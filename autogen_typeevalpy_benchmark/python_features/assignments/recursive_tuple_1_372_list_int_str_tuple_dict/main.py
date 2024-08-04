# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [25, 100, 35]


def func2():
    return 52


def func3():
    return 'oguin'


def func4():
    return (81, 6, 4)


def func5():
    return {'vetar': 25, 'npxkz': 79, 'dzkfc': 43}


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
