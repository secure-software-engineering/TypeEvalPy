#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 58:
            return False
        case False:
            return 58
        case _:
            return "default"


a = func(58)
b = func(False)
c = func({'zepfo': 100, 'kjvla': 75, 'niaoh': 83})
