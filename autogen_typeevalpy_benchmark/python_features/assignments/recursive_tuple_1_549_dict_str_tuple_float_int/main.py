# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ckdex': 24, 'hcyxr': 49, 'ahtlv': 79}


def func2():
    return 'arkqi'


def func3():
    return (29, 17, 61)


def func4():
    return 41.49


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
