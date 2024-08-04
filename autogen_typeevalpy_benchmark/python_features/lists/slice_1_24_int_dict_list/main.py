# A new list is created as a slice of another one containing functions.


def func1():
    return 93


def func2():
    return {'rfnxg': 20, 'dbxdu': 62, 'batsn': 63}


def func3():
    return [41, 49, 85]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
