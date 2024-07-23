# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [39, 91, 81]


def func2():
    return 34


def func3():
    return 81.72


def func4():
    return {'pyzgs': 89, 'yzgrn': 25, 'chxjm': 74}


def func5():
    return (99, 89, 73)


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
