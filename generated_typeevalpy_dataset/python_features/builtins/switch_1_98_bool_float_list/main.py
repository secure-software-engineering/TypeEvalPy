#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 61.87
        case 61.87:
            return False
        case _:
            return "default"


a = func(False)
b = func(61.87)
c = func([15, 87, 80])
