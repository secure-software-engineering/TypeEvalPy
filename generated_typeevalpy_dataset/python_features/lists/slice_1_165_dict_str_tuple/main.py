# A new list is created as a slice of another one containing functions.


def func1():
    return {'uuzvi': 67, 'bakux': 79, 'fldsf': 52}


def func2():
    return 'ivokz'


def func3():
    return (51, 52, 76)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
