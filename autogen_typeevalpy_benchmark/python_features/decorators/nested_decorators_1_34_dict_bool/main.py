# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return {'zgwku': 31, 'csvdt': 96, 'rilti': 46}

    return inner


@dec1
@dec2
def func():
    return True


a = func()
