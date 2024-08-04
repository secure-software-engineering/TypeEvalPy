# The update method of dictionaries is used.


def func1():
    return {'uztpe': 32, 'obkvp': 60, 'titas': 54}


def func2():
    return 20.04


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
