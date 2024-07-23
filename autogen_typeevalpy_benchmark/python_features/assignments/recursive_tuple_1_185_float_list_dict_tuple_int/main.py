# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51.39


def func2():
    return [35, 42, 47]


def func3():
    return {'ldvmp': 81, 'kwjea': 58, 'yhqzx': 37}


def func4():
    return (54, 87, 32)


def func5():
    return 84


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
