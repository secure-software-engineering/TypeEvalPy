# A dictionary key is assigned to a function.


def func1():
    return 88


def func2():
    return (75, 50, 79)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
