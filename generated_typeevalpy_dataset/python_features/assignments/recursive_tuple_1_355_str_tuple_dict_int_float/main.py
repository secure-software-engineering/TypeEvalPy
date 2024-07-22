# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nlirf'


def func2():
    return (72, 69, 49)


def func3():
    return {'fkyni': 20, 'bnimy': 5, 'qdecn': 36}


def func4():
    return 84


def func5():
    return 99.87


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
