# Check if tool type coerces integer and string values.


def func1():
    return {'zregx': 76, 'gpxyj': 97, 'uhrtx': 37}


def func2():
    return (18, 23, 98)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
