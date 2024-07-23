# The update method of dictionaries is used.


def func1():
    return (86, 84, 86)


def func2():
    return 'mvlou'


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
