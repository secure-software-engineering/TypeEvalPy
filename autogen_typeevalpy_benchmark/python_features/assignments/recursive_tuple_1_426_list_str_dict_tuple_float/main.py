# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [25, 44, 12]


def func2():
    return 'rqyqj'


def func3():
    return {'wkjwq': 80, 'qkipb': 37, 'pstky': 18}


def func4():
    return (41, 66, 32)


def func5():
    return 4.96


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
