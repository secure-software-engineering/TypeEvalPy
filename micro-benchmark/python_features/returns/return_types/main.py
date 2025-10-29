# Returning different types


# return_tuple
def func():
    return 1, 2, 3


a = func()


# return_dict
def func1():
    return {"a": 1, "b": 2, "c": 3}


b = func1()

from collections import namedtuple

# return_namedtuple
Point = namedtuple("Point", ["x", "y"])
def func3():
    return Point(1, 2)



c = func3()


# return_set
def func4():
    return set([1, 2, 3, 2, 1])


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
