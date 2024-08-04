# Returning different types


# return_tuple
def func():
    return (73, 96, 94)


a = func()


# return_dict
def func1():
    return {'ytlea': 49, 'blhvo': 63, 'fprri': 28}


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return 75.43


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
