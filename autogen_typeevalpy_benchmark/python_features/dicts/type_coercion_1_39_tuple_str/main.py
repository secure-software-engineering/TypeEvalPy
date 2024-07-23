# Check if tool type coerces integer and string values.


def func1():
    return (39, 32, 1)


def func2():
    return 'npnrn'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
