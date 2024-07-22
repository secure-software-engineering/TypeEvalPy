# A new list is created as a slice of another one containing functions.


def func1():
    return (63, 61, 81)


def func2():
    return [73, 39, 10]


def func3():
    return {'qvchv': 10, 'lrkhg': 18, 'yglvh': 46}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
