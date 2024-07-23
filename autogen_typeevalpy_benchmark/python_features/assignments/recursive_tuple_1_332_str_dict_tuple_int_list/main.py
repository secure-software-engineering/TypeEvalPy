# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jqcaw'


def func2():
    return {'uddth': 55, 'cywqy': 20, 'wcwfs': 89}


def func3():
    return (54, 2, 86)


def func4():
    return 27


def func5():
    return [7, 84, 42]


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
