# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75.69


def func2():
    return 'ivgtf'


def func3():
    return [4, 44, 93]


def func4():
    return {'vllst': 67, 'bcksr': 34, 'wymoo': 21}


def func5():
    return (49, 60, 96)


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
