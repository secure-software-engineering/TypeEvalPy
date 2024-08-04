#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 4
        case 4:
            return False
        case _:
            return "default"


a = func(False)
b = func(4)
c = func({'ldyjy': 89, 'ushdk': 100, 'bdbvt': 75})
