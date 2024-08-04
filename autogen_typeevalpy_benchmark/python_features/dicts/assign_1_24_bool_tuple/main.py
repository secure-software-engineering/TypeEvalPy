# A dictionary key is assigned to a function.


def func1():
    return True


def func2():
    return (20, 25, 70)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
