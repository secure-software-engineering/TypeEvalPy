# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [91, 88, 81]


def func2():
    return {'xylsy': 78, 'wkkmh': 79, 'zbvxa': 58}


def func3():
    return (6, 50, 61)


def func4():
    return 83.41


def func5():
    return 55


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
