# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kkabj'


def func2():
    return [62, 54, 78]


def func3():
    return 93.44


def func4():
    return {'ezgfv': 31, 'cfhjf': 91, 'hvsuf': 69}


def func5():
    return (18, 61, 84)


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
