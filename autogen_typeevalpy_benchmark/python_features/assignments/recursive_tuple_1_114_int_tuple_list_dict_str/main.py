# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return (79, 83, 51)


def func3():
    return [7, 74, 55]


def func4():
    return {'dqzex': 71, 'nlcun': 21, 'quvqg': 42}


def func5():
    return 'fclqp'


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
