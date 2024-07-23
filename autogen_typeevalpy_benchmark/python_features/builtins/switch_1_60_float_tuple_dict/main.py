#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 35.55:
            return (98, 90, 59)
        case (98, 90, 59):
            return 35.55
        case _:
            return "default"


a = func(35.55)
b = func((98, 90, 59))
c = func({'daqtb': 36, 'rcnea': 24, 'sitgc': 46})
