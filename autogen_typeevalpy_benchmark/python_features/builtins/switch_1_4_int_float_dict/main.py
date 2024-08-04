#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 15:
            return 58.16
        case 58.16:
            return 15
        case _:
            return "default"


a = func(15)
b = func(58.16)
c = func({'ozofg': 62, 'aqgoo': 48, 'bqnnt': 30})
