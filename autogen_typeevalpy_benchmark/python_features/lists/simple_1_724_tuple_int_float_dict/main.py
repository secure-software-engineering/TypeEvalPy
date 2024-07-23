# Functions are assigned as elements of a list and then called.


def func1():
    return (19, 91, 72)


def func2():
    return 49


def func3():
    return 38.41


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rjvtg': 96, 'nuztu': 26, 'bizyd': 98}


b = ["Hello"]
b[0] = func4

f = b[0]()
