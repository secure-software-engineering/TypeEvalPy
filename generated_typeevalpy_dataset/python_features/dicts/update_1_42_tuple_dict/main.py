# The update method of dictionaries is used.


def func1():
    return {'rhkzl': 86, 'eaybl': 19, 'nhsmu': 39}


def func2():
    return (32, 47, 42)


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
