# A new list is created as a slice of another one containing functions.


def func1():
    return 74


def func2():
    return False


def func3():
    return {'riuce': 37, 'kygvg': 67, 'tcymd': 57}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
