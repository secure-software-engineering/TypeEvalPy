# A new list is created as a slice of another one containing functions.


def func1():
    return 75.3


def func2():
    return {'pjkxn': 88, 'utffo': 74, 'ovzek': 11}


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
