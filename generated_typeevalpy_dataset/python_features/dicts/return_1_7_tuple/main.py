# A dictionary is returned.


def func2():
    return (49, 14, 31)


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()
