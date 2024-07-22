# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21.35


def func2():
    return {'sqygk': 2, 'lbwtw': 31, 'emicr': 31}


def func3():
    return (2, 89, 60)


def func4():
    return 43


def func5():
    return [85, 54, 61]


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
