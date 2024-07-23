# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [37, 11, 65]


def func2():
    return 44.63


def func3():
    return {'duxhr': 92, 'zqsub': 89, 'tggad': 48}


def func4():
    return (74, 59, 87)


def func5():
    return 'jejrx'


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
