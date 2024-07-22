# A new list is created as a slice of another one containing functions.


def func1():
    return {'yqnik': 4, 'gjrrw': 99, 'ywhzk': 25}


def func2():
    return [36, 32, 57]


def func3():
    return 'tniuh'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
