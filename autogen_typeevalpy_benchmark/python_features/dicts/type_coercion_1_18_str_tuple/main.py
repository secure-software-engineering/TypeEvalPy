# Check if tool type coerces integer and string values.


def func1():
    return 'xzxdi'


def func2():
    return (54, 62, 26)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
