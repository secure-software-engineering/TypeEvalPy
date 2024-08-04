# A new list is created as a slice of another one containing functions.


def func1():
    return {'oraxz': 68, 'yddrl': 65, 'rrevs': 69}


def func2():
    return (78, 93, 61)


def func3():
    return 79.75


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
