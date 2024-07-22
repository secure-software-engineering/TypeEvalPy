# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (75, 67, 29)


def func2():
    return 92.44


def func3():
    return {'bxlvf': 56, 'tqeog': 74, 'npdau': 9}


def func4():
    return 'zbhsd'


def func5():
    return [91, 30, 75]


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
