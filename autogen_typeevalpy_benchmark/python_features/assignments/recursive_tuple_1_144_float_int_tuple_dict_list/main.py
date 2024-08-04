# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25.8


def func2():
    return 5


def func3():
    return (96, 10, 57)


def func4():
    return {'tpvyi': 68, 'sjzof': 25, 'glhfe': 12}


def func5():
    return [75, 4, 81]


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
