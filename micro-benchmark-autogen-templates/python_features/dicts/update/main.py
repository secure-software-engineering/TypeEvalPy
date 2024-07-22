# The update method of dictionaries is used.


def func1():
    return <value2>


def func2():
    return <value1>


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
