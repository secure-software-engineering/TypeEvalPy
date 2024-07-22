# A new list is created as a slice of another one containing functions.


def func1():
    return 'qugrt'


def func2():
    return 49


def func3():
    return {'qmskr': 6, 'bijtr': 56, 'bvmex': 78}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
