# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (32, 83, 20)


def func2():
    return {'dhbsc': 42, 'iikrz': 23, 'ebovi': 97}


def func3():
    return 84


def func4():
    return 'mibdj'


def func5():
    return [63, 93, 9]


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
