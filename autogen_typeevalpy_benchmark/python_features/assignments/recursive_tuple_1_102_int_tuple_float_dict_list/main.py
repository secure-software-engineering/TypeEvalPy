# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 78


def func2():
    return (84, 67, 99)


def func3():
    return 34.8


def func4():
    return {'uijwl': 19, 'xukfp': 99, 'bdqmu': 40}


def func5():
    return [71, 12, 64]


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
