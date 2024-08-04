# A new list is created as a slice of another one containing functions.


def func1():
    return {'jbtoe': 69, 'nunaj': 28, 'hzaiy': 47}


def func2():
    return False


def func3():
    return 23


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
