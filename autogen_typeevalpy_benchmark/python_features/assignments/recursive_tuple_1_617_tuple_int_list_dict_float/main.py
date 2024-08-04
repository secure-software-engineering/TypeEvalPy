# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 30, 55)


def func2():
    return 5


def func3():
    return [49, 52, 60]


def func4():
    return {'pqnhb': 68, 'jivzw': 50, 'retye': 24}


def func5():
    return 17.41


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
