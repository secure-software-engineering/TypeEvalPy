# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5.65


def func2():
    return (69, 47, 70)


def func3():
    return [30, 89, 68]


def func4():
    return {'eerqw': 50, 'fysoy': 67, 'lfbzk': 54}


def func5():
    return 61


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
