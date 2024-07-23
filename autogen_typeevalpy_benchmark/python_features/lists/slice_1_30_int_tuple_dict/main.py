# A new list is created as a slice of another one containing functions.


def func1():
    return 65


def func2():
    return (57, 57, 69)


def func3():
    return {'ylcei': 99, 'clzid': 97, 'opwdd': 28}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
