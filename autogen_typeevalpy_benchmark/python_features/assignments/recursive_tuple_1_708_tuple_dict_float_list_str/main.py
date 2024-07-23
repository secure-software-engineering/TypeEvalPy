# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (26, 22, 51)


def func2():
    return {'dnutw': 30, 'csyti': 58, 'qnmua': 8}


def func3():
    return 28.34


def func4():
    return [77, 32, 1]


def func5():
    return 'rmlnh'


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
