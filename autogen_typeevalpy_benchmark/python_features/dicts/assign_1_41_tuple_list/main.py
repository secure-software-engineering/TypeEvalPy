# A dictionary key is assigned to a function.


def func1():
    return (53, 5, 2)


def func2():
    return [77, 2, 94]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
