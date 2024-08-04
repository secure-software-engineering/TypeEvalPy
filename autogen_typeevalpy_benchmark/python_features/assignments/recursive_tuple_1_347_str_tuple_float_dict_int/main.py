# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ssjtt'


def func2():
    return (88, 56, 20)


def func3():
    return 69.1


def func4():
    return {'vejea': 92, 'evkce': 67, 'bklse': 92}


def func5():
    return 72


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
