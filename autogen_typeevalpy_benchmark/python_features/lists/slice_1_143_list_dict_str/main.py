# A new list is created as a slice of another one containing functions.


def func1():
    return [77, 79, 54]


def func2():
    return {'aqsqe': 9, 'ffpla': 58, 'hdauj': 99}


def func3():
    return 'fcbnp'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
