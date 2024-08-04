# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xcoea': 7, 'askes': 75, 'bkaxx': 47}


def func2():
    return (56, 25, 24)


def func3():
    return 'bvqag'


def func4():
    return [10, 7, 95]


def func5():
    return 98


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
