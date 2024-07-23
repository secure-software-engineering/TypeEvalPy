#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 87:
            return (16, 78, 43)
        case (16, 78, 43):
            return 87
        case _:
            return "default"


a = func(87)
b = func((16, 78, 43))
c = func(65.89)
