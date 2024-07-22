# A new list is created as a slice of another one containing functions.


def func1():
    return {'leofv': 58, 'vvjnf': 16, 'upvju': 86}


def func2():
    return True


def func3():
    return [92, 13, 22]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
