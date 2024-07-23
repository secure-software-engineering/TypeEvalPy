# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [55, 11, 73]


def func2():
    return 44


def func3():
    return (20, 83, 40)


def func4():
    return {'qemft': 75, 'myhib': 52, 'rlnwz': 29}


def func5():
    return 39.65


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
