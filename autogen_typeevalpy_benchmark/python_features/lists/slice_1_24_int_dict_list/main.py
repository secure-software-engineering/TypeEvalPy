# A new list is created as a slice of another one containing functions.


def func1():
    return 38


def func2():
    return {'ktzwe': 53, 'qqfnh': 53, 'pahze': 6}


def func3():
    return [91, 31, 61]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
