# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5.56


def func2():
    return {'matwz': 25, 'nirsg': 31, 'oqeqa': 41}


def func3():
    return (33, 70, 69)


def func4():
    return [53, 18, 25]


def func5():
    return 91


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
