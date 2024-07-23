# A new list is created as a slice of another one containing functions.


def func1():
    return 36.34


def func2():
    return 'mqwye'


def func3():
    return [26, 49, 8]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
