#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 87
        case 87:
            return False
        case _:
            return "default"


a = func(False)
b = func(87)
c = func(47.66)
