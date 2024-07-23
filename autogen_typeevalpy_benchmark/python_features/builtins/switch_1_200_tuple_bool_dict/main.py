#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (37, 71, 45):
            return False
        case False:
            return (37, 71, 45)
        case _:
            return "default"


a = func((37, 71, 45))
b = func(False)
c = func({'ypdae': 63, 'idaqo': 25, 'kbbwt': 4})
