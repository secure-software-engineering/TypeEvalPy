# Check if tool type coerces integer and string values.


def func1():
    return (54, 40, 69)


def func2():
    return 'lhfrd'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
