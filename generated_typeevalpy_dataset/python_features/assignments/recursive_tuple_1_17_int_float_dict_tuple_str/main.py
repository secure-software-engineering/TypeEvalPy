# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 78


def func2():
    return 21.03


def func3():
    return {'rgtmf': 66, 'ulygo': 61, 'nswwv': 31}


def func4():
    return (75, 37, 80)


def func5():
    return 'fzjrj'


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
