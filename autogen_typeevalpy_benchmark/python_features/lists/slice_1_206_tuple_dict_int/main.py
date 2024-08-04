# A new list is created as a slice of another one containing functions.


def func1():
    return (75, 44, 94)


def func2():
    return {'bqmkr': 78, 'exfrc': 58, 'xftar': 68}


def func3():
    return 41


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
