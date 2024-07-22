# A dictionary key is assigned to a function.


def func1():
    return 'ytkbh'


def func2():
    return 81.46


d = {"a": func1}

d["a"] = func2

e = d["a"]()
