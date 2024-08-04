# Check if tool type coerces integer and string values.


def func1():
    return {'aynjc': 57, 'ngfvf': 79, 'glbzn': 81}


def func2():
    return 91.99


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
