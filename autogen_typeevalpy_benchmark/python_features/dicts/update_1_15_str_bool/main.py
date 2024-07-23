# The update method of dictionaries is used.


def func1():
    return True


def func2():
    return 'ljujt'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
