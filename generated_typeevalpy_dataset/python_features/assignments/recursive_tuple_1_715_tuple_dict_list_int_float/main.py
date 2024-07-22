# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (48, 58, 50)


def func2():
    return {'sinqn': 67, 'pjrkm': 92, 'rwgzg': 63}


def func3():
    return [50, 83, 94]


def func4():
    return 51


def func5():
    return 85.38


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
