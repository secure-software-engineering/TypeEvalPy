# A dictionary key is assigned to a function.


def func1():
    return (49, 97, 38)


def func2():
    return [12, 33, 38]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
