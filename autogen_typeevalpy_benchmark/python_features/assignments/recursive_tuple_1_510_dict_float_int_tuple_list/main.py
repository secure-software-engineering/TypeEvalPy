# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vqeqh': 93, 'telbr': 14, 'qarif': 29}


def func2():
    return 65.82


def func3():
    return 98


def func4():
    return (6, 6, 35)


def func5():
    return [74, 69, 29]


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
