#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [41, 85, 21]:
            return 47
        case 47:
            return [41, 85, 21]
        case _:
            return "default"


a = func([41, 85, 21])
b = func(47)
c = func({'fcmie': 81, 'lnyiq': 48, 'nthvy': 45})
