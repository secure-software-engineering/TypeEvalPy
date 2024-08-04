# A new list is created as a slice of another one containing functions.


def func1():
    return {'woyzs': 23, 'xjqzc': 7, 'ssufk': 53}


def func2():
    return 83


def func3():
    return 80.55


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
