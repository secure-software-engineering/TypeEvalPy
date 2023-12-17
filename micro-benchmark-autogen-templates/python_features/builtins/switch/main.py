#  A function is defined with switch statement in it.
def func(value):
    match value:
        case "case1":
            return 42
        case "case2":
            return "hello this is case2"
        case _:
            return "unknown type"


a = func("case1")
b = func("case2")
c = func("case3")
