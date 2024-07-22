# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [26, 17, 56]


def func2():
    return 'lunix'


def func3():
    return {'xuslj': 32, 'ropzc': 93, 'zaigu': 49}


def func4():
    return (25, 50, 87)


def func5():
    return 59


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
