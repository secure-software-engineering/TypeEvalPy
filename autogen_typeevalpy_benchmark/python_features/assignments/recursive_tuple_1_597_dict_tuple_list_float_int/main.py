# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zxion': 15, 'jihki': 84, 'vigjn': 38}


def func2():
    return (16, 14, 54)


def func3():
    return [29, 14, 92]


def func4():
    return 68.72


def func5():
    return 93


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
