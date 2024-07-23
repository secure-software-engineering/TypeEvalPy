# A new list is created as a slice of another one containing functions.


def func1():
    return {'vpcvk': 36, 'unfwh': 2, 'mcrfz': 21}


def func2():
    return [33, 80, 91]


def func3():
    return (88, 19, 19)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
