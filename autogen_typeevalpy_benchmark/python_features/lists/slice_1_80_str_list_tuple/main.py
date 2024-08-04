# A new list is created as a slice of another one containing functions.


def func1():
    return 'dknjl'


def func2():
    return [26, 15, 20]


def func3():
    return (9, 100, 80)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
