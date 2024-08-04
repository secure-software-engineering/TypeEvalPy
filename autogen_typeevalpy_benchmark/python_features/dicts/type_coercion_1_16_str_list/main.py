# Check if tool type coerces integer and string values.


def func1():
    return 'ozvza'


def func2():
    return [89, 66, 92]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
