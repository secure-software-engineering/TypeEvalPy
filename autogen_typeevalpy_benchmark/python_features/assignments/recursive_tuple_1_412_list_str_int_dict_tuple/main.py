# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [34, 53, 11]


def func2():
    return 'arojk'


def func3():
    return 74


def func4():
    return {'fxzho': 6, 'jnzbu': 99, 'zmcgk': 79}


def func5():
    return (23, 1, 57)


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
