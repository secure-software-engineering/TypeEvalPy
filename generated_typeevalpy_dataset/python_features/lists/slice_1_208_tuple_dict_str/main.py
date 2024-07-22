# A new list is created as a slice of another one containing functions.


def func1():
    return (44, 15, 82)


def func2():
    return {'hsikr': 18, 'tugvv': 58, 'uppon': 54}


def func3():
    return 'idtce'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
