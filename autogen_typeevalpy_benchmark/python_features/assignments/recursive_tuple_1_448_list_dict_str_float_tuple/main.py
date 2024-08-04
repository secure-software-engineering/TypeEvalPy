# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [14, 71, 45]


def func2():
    return {'rjvbl': 81, 'napdw': 52, 'maoyb': 29}


def func3():
    return 'yxkyl'


def func4():
    return 21.92


def func5():
    return (18, 36, 61)


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
