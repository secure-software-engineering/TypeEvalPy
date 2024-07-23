# Check if tool type coerces integer and string values.


def func1():
    return False


def func2():
    return {'daruy': 90, 'mgxpg': 59, 'xrali': 95}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
