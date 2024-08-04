# A new list is created as a slice of another one containing functions.


def func1():
    return 40


def func2():
    return (67, 56, 4)


def func3():
    return {'qjzdc': 94, 'akxbd': 46, 'smpif': 53}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
