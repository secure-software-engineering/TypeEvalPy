# A new list is created as a slice of another one containing functions.


def func1():
    return 83


def func2():
    return {'awbxf': 49, 'djmcj': 61, 'gjbml': 31}


def func3():
    return (44, 89, 59)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
