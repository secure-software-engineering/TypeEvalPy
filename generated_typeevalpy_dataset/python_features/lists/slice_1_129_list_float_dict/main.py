# A new list is created as a slice of another one containing functions.


def func1():
    return [3, 75, 75]


def func2():
    return 11.03


def func3():
    return {'awlen': 61, 'spdgf': 57, 'qiram': 47}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
